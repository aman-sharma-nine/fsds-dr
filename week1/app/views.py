from app import app
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd 
import joblib 
import numpy as np



@app.route('/', methods =["GET"])
def index():
        return render_template('index.html')


@app.route('/predict', methods =['POST','GET'])
def predict_():
        if request.method == "POST":
                with open(f'/Users/aman.sharma/github/fsds-dr/week1/app/xgboost.joblib', 'rb') as f:
                        model = joblib.load(f)
                cols = ['FlightDate', 'DepTime', 'UniqueCarrier', 'Origin', 'Dest', 'Distance', 'Day_of_Week']
                flightdate = request.form['fdate']
                depdate = request.form['ddate']
                carrier = request.form['carrier']
                origin = request.form['origin']
                destination = request.form['dest']
                distance = request.form['dist']
                dayofweek = request.form['dow']
                #prediction = [x for x in request.form.values()]
                #input_data = list(prediction)
                #pred_array =  np.array(input_data)
                score_df = pd.DataFrame([[flightdate, depdate, carrier, origin, destination, distance, dayofweek]], columns=cols)
                score = model.predict_proba(score_df)[0]
                return render_template("predict.html", prediction_text = "The prediction is {}".format(score))
                
                # to view the response in the browser
                #print (request.form)
                #return jsonify(request.form.to_dict())
                
                
        else:
                return render_template("index.html")

