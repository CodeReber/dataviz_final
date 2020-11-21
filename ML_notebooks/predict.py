import pickle
import joblib as joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

co2 = 22
seaice = 31
temp  = 142
rsf_pred = ""
loaded_model = joblib.load("rf_rsf.sav")

def random_forest(co2, seaice, temp):
    # 10 climate variables
    X_test = [340, co2, 450, 23, 23, seaice, 1232, 123, temp, 23]
    Ypredict = loaded_model.predict(X_test)  
    print(Ypredict)

