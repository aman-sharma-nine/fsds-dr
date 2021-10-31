from app import app
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd 
import joblib 
import numpy as np
import os

# upload folder 
upload_folder = 'static/files'
app.config["UPLOAD_FOLDER"] = upload_folder

path_to_model = "{}/xgboost.joblib".format(os.getcwd())
with open(path_to_model, 'rb') as f:
        model = joblib.load(f)


# Home page route - when user hits the /
@app.route('/', methods =["GET"])
def index():
        return render_template('index.html')

# Routes to /predict url when user click predict 
@app.route('/predict', methods =['POST','GET'])
def predict_():
        if request.method == "POST":
                #with open(f'/Users/aman.sharma/github/fsds-dr/week1/app/xgboost.joblib', 'rb') as f:
                #        model = joblib.load(f)
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
                score = model.predict_proba(score_df)[0][0]
                return render_template("predict.html", prediction_text = "The prediction is {}".format(score))
                
                # to view the response in the browser
                #print (request.form)
                #return jsonify(request.form.to_dict())
                
                
        else:
                return render_template("index.html")
#We're veryfying the request method is POST with if request.method == "POST":
#We then veryfy if the request contains files with if request.files:
#We then store the file as a variable called image using image = request.files["image"]
## NOT WORKING 
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
         #We use file_.filename to access the filename of the image and join that with the path to the uploads folder with os.join().
            #file_.save(os.path.join(app.config["FILE_UPLOADS"], file_.filename))
    if request.method == "POST":
        if request.files:
            uploaded_file = request.files["batchfilename"]
            if uploaded_file.filename !='':
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                    uploaded_file.save(file_path)
                    scoring_file = pd.read_csv(file_path)
                    batch_score = model.predict_proba(scoring_file)[0]
                    return render_template('upload.html')
        
        return redirect (url_for('index'))


           
