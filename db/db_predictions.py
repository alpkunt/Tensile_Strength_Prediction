from sqlalchemy.orm import Session
from schemas import UserBase, UserUpdate
from db.models import User, Tensile_Strength_Predictions
from db.hash import Hash
from fastapi import HTTPException, status
from enum import Enum
import joblib
from sklearnex import patch_sklearn

patch_sklearn()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from numpy import mean, std
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import HistGradientBoostingRegressor
import xgboost as xgb

xgb_predictor = xgb.XGBRegressor()

###### ---- Load Models ----- ######


rf_predictor = joblib.load("pred_models/GridSearchRF.pkl")
lgbm_predictor = joblib.load("pred_models/GridSearchLGBM.pkl")
hgbr_predictor = joblib.load("pred_models/GridSearchHGBR.pkl")
xgb_predictor.load_model("pred_models/GridSearchXGB.json")

loaded_models_dict = {
    "RF": rf_predictor,
    "LGBM": lgbm_predictor,
    "HGBR": hgbr_predictor,
    "XGB": xgb_predictor
}

predict_array3 = [
    [863, 660, 780, 0.5, 0.19, 0.8, 0.011, 0.013, 0.03, 0.03, 0.01, 0.0]]  # bunu mecbur vectore çevireceğiz unutma!!


def insert_prediction_to_db(model, composition, prediction, db: Session, current_user):
    new_prediction = Tensile_Strength_Predictions(
        composition=composition,
        prediction_method=model,
        prediction_result=prediction,
        user_id=current_user.id
    )
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    #return new_prediction
    return {"db" : "ok"}

def prediction_by_composition(chosen_model, request, db: Session, current_user):  # bakalım sonra type hint yaparız!
    # predict array requestten gelecek, onu çevirmek gerekecek numpy arraye!

    _, unzipped = zip(*list(request)) #requesti list olarak çekiyorum!,
    # bu şekilde bir  [('NT', 863.0), ('QT', 660.0), ('TT', 780.0),.... ] liste olarak geliyor!
    # _ ve unzipped için tekrar 2 listeye ayırıyorum, sonrasında da tekrar liste construct edip 2d array yapmış olacağım!

    requested_composition = np.array(list(unzipped)).reshape(1,-1)
    #print("asdsaddasddasdasd", np.array(requested_composition).reshape(1,-1))
    elements = ["NT", "QT", "TT", "C", "Si", "Mn", "P", "S", "Ni", "Cr", "Cu", "Mo"]

    warning = "No model is selected"
    model = loaded_models_dict.get(chosen_model, warning)
    if model != warning:
        prediction = model.predict(requested_composition).tolist()
        return {
            "model": chosen_model,
            "composition": zip(elements, requested_composition[0]),
            "prediction": prediction[0],
            "current_user" : current_user,
            "act": insert_prediction_to_db(model=chosen_model,
                                           composition=dict(zip(elements, requested_composition[0])),
                                           # dikkat burda dict constructor var!
                                           prediction=prediction[0],
                                           db=db,
                                           current_user=current_user
                                           )
        }
    else:
        return {"data": warning}
