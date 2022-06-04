# Standard libraries imports
import os
import json

# Third party libraries imports
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

# Local imports
from app.models import User
from app.routes import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
