from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///market.db'
#db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)