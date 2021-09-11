from app import app 
from flask import Flask, render_template, request, redirect
import pandas as pd 
import joblib 
import numpy as np

model = joblib.load('/Users/aman.sharma/github/fsds-dr/week1/app/xgboost.joblib')

@app.route("/", methods =["GET", "POST"])
def index():
        req_type = request.method
        if req_type =="GET":
                return render_template("index.html")
        else:
                dest= request.form['dest']
                return dest.upper()
'''def predict():
        input_features = [float(x) for x in request.form.values()]
        #feat_array = [np.array(input_features)]
        #scoring_data = pd.DataFrame([feat_array], columns = cols)
        #prediction = model.predict_proba(feat_array)
        #output = (prediction)

        return render_template("index.html")'''

