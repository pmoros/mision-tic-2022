from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    profile_pic = db.Column(db.String(255), nullable=False)

class ProductLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    products = db.relationship("Product", backref="product", uselist=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    availabe = db.Column(db.Float, nullable=False)
    store = db.Column(db.Float, nullable=False)
    productLine_id = db.Column(db.Integer, db.ForeignKey('product_line.id'), nullable=False)

def load_test_data():
    # User test data
    test_user = User(sub='123456', name='testName',
                     email='testEmail', profile_pic='testPic')
    db.session.add(test_user)
    db.session.commit()
