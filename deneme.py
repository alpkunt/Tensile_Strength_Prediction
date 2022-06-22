import joblib
from sklearnex import patch_sklearn
patch_sklearn()
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from numpy import mean, std
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import GridSearchCV
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor

import xgboost as xgb
xgb_predictor = xgb.XGBRegressor()

predict_array = [[865,865,550,0.35,0.21,0.77,0.021,0.022,0.01,0.01,0.02,0.0]]
predict_array2 = [[865,120,1250,0.1,0.21,0.75,0.031,0.019,0.01,0.09,0.02,0.0]]

rf_predictor = joblib.load("pred_models/GridSearchRF.pkl")
lgbm_predictor = joblib.load("pred_models/GridSearchLGBM.pkl")
hgbr_predictor = joblib.load("pred_models/GridSearchHGBR.pkl")
xgb_predictor.load_model("pred_models/GridSearchXGB.json")

print("RF predictor :", rf_predictor.predict(predict_array))
print("LGBM predictor :", lgbm_predictor.predict(predict_array))
print("XGBoost predictor :", xgb_predictor.predict(predict_array))
print("HistGradientBoosting predictor :", hgbr_predictor.predict(predict_array))
