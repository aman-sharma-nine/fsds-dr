from app import app 

@app.route("/predict", methods =["GET","POST"])
def predict():
        return ("TEST ")
