from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    profile_pic = db.Column(db.String(255), nullable=False)


def load_test_data():
    # User test data
    test_user = User(name='testName', email='testEmail', profile_pic='testPic')
    db.session.add(test_user)
    db.session.commit()
