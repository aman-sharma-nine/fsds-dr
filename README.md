# Full Stack Data Science 

## Moving Pipeline to remote server 

- Create a model and pipeline on the local machine 
- Moving the mode to EC2 instance 
 - Create a new ec2 instance 
 - Launch EC2 instance 
 - SSH into remote server : ssh -L localhost:8888:localhost:8888 ubuntu@<your-IP>
 - Transfer your project files to remote host 
  - `mkdir fsds`
  - cd mkdir 



## Building Flask application 
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


## Move tha flask application to Heroku
 - Create Git Repo
 - Log in to heroku 
 - Create PROC file - tells heroku where to start the application 
 - create requirement.txt - to install dependencies
    `pip list --format=freeze > requirements.txt`





https://www.kdnuggets.com/2020/05/build-deploy-machine-learning-web-app.html


#### Helper
        Python specific serialization :
                - Comparison between pickle, joblib and pmml/onnx


