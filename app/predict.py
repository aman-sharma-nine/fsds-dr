from app import app 
from flask import Flask, render_template, request, redirect
import pandas as pd 
import joblib 
import numpy as np


path_to_model = "{}/xgboost.joblib".format(os.getcwd())
with open(path_to_model, 'rb') as f:
        model = joblib.load(f)

cols = ['FlightDate', 'DepTime', 'UniqueCarrier', 'Origin', 'Dest', 'Distance', 'Day_of_Week']


@app.route("/predict", methods =["GET", "POST"])
def predict_():
        prediction = [x for x in request.form.values()]
        pred_array =  np.array(prediction)
        score_df = pd.DataFrame([pred_array])
        score = model.predict_proba(score_df)
        return render_template("index.html", prediction_text = "The prediction is {}".format(score))
