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
from enum import Enum


import xgboost as xgb
xgb_predictor = xgb.XGBRegressor()

predict_array = [[865,865,550,0.35,0.21,0.77,0.021,0.022,0.01,0.01,0.02,0.0]]
predict_array2 = [[865,120,1250,0.1,0.21,0.75,0.031,0.019,0.01,0.09,0.02,0.0]]

predict_array3 = [[863,660,780,0.5,0.19,0.8,0.011,0.013,0.03,0.03,0.01,0.0 ]]

print(len(predict_array[0]))
print(len(predict_array3[0]))


rf_predictor = joblib.load("pred_models/GridSearchRF.pkl")
lgbm_predictor = joblib.load("pred_models/GridSearchLGBM.pkl")
hgbr_predictor = joblib.load("pred_models/GridSearchHGBR.pkl")
xgb_predictor.load_model("pred_models/GridSearchXGB.json")

print("RF predictor :", rf_predictor.predict(predict_array))
print("LGBM predictor :", lgbm_predictor.predict(predict_array))
print("XGBoost predictor :", xgb_predictor.predict(predict_array))
print("HistGradientBoosting predictor :", hgbr_predictor.predict(predict_array))



print("RF predictor 3 :", rf_predictor.predict(predict_array3))
print("LGBM predictor 3 :", lgbm_predictor.predict(predict_array3))
print("XGBoost predictor 3 :", xgb_predictor.predict(predict_array3))
print("HistGradientBoosting predictor 3 :", hgbr_predictor.predict(predict_array3))





