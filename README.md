# Full Stack Data Science 

## Week 1

## Week 2 

## Week 3

#### Tasks:
- Train and validate models and develop a machine learning pipeline for deployment.
- Build a basic HTML front-end with an input form for independent variables
- Build a back-end of the web application using a Flask Framework.
- Deploy the web app on Heroku. Once deployed, it will become publicly available and can be accessed via  Web URL.

#### Notes:

Task 2 - Building front end web application 
I used HTML basic framework to delevelop a simple web UI. 

Task3 - Back End of web application using Flask 

To DO :
- build a form to input scoring data 
- Save the inpute features in an array 
- load the model pipeline .joblib
- put the array to model.predict_proba
- save the prediction values in a variable 
- return that variable 

https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/


https://www.kdnuggets.com/2020/05/build-deploy-machine-learning-web-app.html


#### Assignment
        Data set for scoring
        Get running a prebuilt Flask web app on your remote server  that includes a pre built model on your server (Code is here). 
        Keep the two routes. One for UI, one for batch predictions.
        Manipulate the Flask web app to use your model pipeline and deploy to your remote server (Digital Ocean). You should be able to do UI predictions and batch predictions. 
        Submission Criteria: Send the endpoint back to Tony & Theo
        Optional 1: Set up a batch scoring job that can send the scored data to a remote server.
                        Submission Criteria: predictions sent to “data server”
        Optional 2: Use Heroku to deploy the application but serve the model in Digital Ocean.

#### Helper
        Python specific serialization :
                - Comparison between pickle, joblib and pmml/onnx


