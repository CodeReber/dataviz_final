import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
co2 = 300
seaice = 4
temp  = 30
rsf_pred = “”
def random_forest(co2, seaice, temp):
    loaded_model = joblib.load(“rf_rsf.sav”)
    # 10 climate variables
    X_test = [340, co2, 450, 23, 23, seaice, 1232, 123, temp]
    Ypredict = joblib_LR_model.predict(X_test)
    rsf_pred = Ypredict