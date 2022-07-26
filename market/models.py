from market import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable = False)
    email_address= db.Column(db.String(50), nullable=False,unique =True)
    password_hash= db.Column(db.String(60),nullable=False)
    wallet = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'Item {self.user_id}'




class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(30), nullable=False, unique=True)
    item_code = db.Column(db.Integer, nullable=False)
    item_price = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Item {self.item_id}'