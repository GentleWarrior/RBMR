from scriptspy import db
from flask_login import UserMixin


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
    personal = db.relationship("Personal", backref='User', lazy=True)
    contact = db.relationship('Contact', backref = 'User', lazy=True)

class Personal(db.Model, UserMixin):
    personal_id = db.Column(db.Integer, primary_key=True)
    DOB = db.Column(db.Text)
    Gender = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Contact(db.Model, UserMixin):
    contact_id = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.Text(150))
    City = db.Column(db.String(150))
    District = db.Column(db.String(150))
    Phone = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)