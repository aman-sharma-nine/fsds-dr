from joblib import load 
import pandas as pd
import xgboost 

score = pd.read_csv('data/airline_delay_test_new.csv')
X = score.drop('dep_delayed_15min', axis=1)

pipeline = load("xgboost.joblib")

result = pipeline.predict_proba(X)
print(result)


