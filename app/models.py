import enum
from flask_login import UserMixin
from app import db


class UserChoices(enum.Enum):
    VENDOR = 'VENDOR'
    CUSTOMER = 'CUSTOMER'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    profile_pic = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum(UserChoices))
    order_vendor = db.relationship(
        "Order", backref="order_vendor", uselist=False,  primaryjoin="User.id == Order.vendor_id")
    order_customer = db.relationship(
        "Order", backref="order_customer", uselist=False,  primaryjoin="User.id == Order.customer_id")
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=True)
    city = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)


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
    image = db.Column(db.String(500), nullable=False)
    available = db.Column(db.Boolean, default=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    productLine_id = db.Column(db.Integer, db.ForeignKey(
        'product_line.id'), nullable=False)
    orderDetalls = db.relationship(
        "OrderDetail", backref="order_detail", uselist=False)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    stores = db.relationship("Store", backref="store", uselist=False)
    users = db.relationship("User", backref="user", uselist=False)


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    county = db.Column(db.String(255), nullable=False)
    users = db.relationship("User", backref="user_vendor", uselist=False)
    products = db.relationship(
        "Product", backref="offered_product", uselist=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    required_date = db.Column(db.DateTime, nullable=False)
    shipped_date = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    Confirmed = db.Column(db.Boolean, default=False, nullable=False)
    accepted = db.Column(db.Boolean, default=False, nullable=False)
    orderDetails = db.relationship(
        "OrderDetail", backref="order_details", uselist=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    customer_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)


class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


def load_test_data():
    # User test data
    test_user = User(sub='123456', name='testName',
                     email='testEmail', profile_pic='testPic')
    db.session.add(test_user)
    db.session.commit()
