import bcrypt
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://vyltqkbfwiatos:202dab04b98cbf1832199a50aa1c1c34abfeda28cda45efb92416c0a1a34ea8e@ec2-3-223-242-224.compute-1.amazonaws.com:5432/da8l04fvu1icuj'

app.config['SECRET_KEY']= 'ff648669200685e80e1de9eb'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category ="danger"
from market import route 

