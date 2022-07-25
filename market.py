from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
app = Flask(__name__)
db = SQLAlchemy(app)

class Item(db.Model):
    ITEMID = db.Column(db.Integer, primary_key=True)
    ITEMNAME = db.Column(db.String(30), nullable=False, unique=True)
    ITEMCODE = db.Column(db.Integer, nullable=False)
    ITEMPRICE = db.Column(db.String(30), nullable=False, unique=True)
    Description = db.Column(db.String(1024), nullable=False, unique=True)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
         {'ITEMID' : 1, 'ITEMNAME': 'Mobilephone', 'ITEMCODE':'101', 'ITEMPRICE':10000},
         {'ITEMID' : 2, 'ITEMNAME': 'Backpack', 'ITEMCODE':'102', 'ITEMPRICE':500},
         {'ITEMID' : 3, 'ITEMNAME': 'Laptop', 'ITEMCODE':'103', 'ITEMPRICE': 50000},
         {'ITEMID' : 4, 'ITEMNAME': 'keyboard', 'ITEMCODE':'104', 'ITEMPRICE':2000},
         {'ITEMID' : 5, 'ITEMNAME': 'furniture', 'ITEMCODE':'105', 'ITEMPRICE':20000} ]
    return render_template('market.html',items=items)







if __name__ == "__main__":
    app.run(debug=True)