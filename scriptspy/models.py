from scriptspy import db
from flask_login import UserMixin
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    DOB = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    address = db.Column(db.varChar(150))
    phone = db.Column(db.Integer(150))

