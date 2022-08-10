import bcrypt
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://ecomm:ecomm@localhost:5432/ecomm'
app.config['SECRET_KEY']= 'ff648669200685e80e1de9eb'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager = LoginManager(app)
from market import route 
