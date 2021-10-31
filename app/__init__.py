from flask import Flask 
import joblib

app = Flask(__name__)

from app import views
from app import views_about


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)