from flask import Flask 
import joblib

app = Flask(__name__)

from app import views
from app import views_about
from app import predict

model = joblib.load('/Users/aman.sharma/github/fsds-dr/week1/app/xgboost.joblib')
