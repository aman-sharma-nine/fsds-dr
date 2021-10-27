# Full Stack Data Science 

## Week 1

## Week 2 

## Week 3

#### Tasks:
- Train and validate models and develop a machine learning pipeline for deployment. - DONE
- Build a basic HTML front-end with an input form for independent variables - DONE 
- Build a back-end of the web application using a Flask Framework. - DONE
- Batch predictions - 
- Deploy the web app on Heroku. Once deployed, it will become publicly available and can be accessed via  Web URL.

#### Notes:

Task 2 - Building front end web application 
I used HTML basic framework to delevelop a simple web UI. 

Task3 - Back End of web application using Flask 

To DO :
- build a form to input scoring data - DONE
- Save the inpute features in an array  - DONE
        The most important thing to know about this form is that it performs a POST request to the same route that generated the form. The keys that will be read in the app all come from the name attributes on our form inputs. In this case, language and framework are the names of the inputs, so you will have access to those in the ap
- load the model pipeline .joblib - DONE
- put the array to model.predict_proba - DONE
- save the prediction values in a variable - DONE
- return that variable - DONE 
- Change the route to /predict when "Predict" button is pressed - DONE
- Add functionality to upload a file then run bacth scoring - TO DO

https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
#### Heroku set up 
 - Make sure you have brew installed 
 - Create Heroku login 



https://www.kdnuggets.com/2020/05/build-deploy-machine-learning-web-app.html


#### Assignment
        Data set for scoring
        Get running a prebuilt Flask web app on your remote server  that includes a pre built model on your server (Code is here). - DONE
        Keep the two routes. One for UI, one for batch predictions.
        Manipulate the Flask web app to use your model pipeline and deploy to your remote server (Digital Ocean). You should be able to do UI predictions and batch predictions. 
        Submission Criteria: Send the endpoint back to Tony & Theo
        Optional 1: Set up a batch scoring job that can send the scored data to a remote server.
                        Submission Criteria: predictions sent to “data server”
        Optional 2: Use Heroku to deploy the application but serve the model in Digital Ocean.

#### Helper
        Python specific serialization :
                - Comparison between pickle, joblib and pmml/onnx


