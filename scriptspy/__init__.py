from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
DB_NAME = "DONORS.db"


def create_app():
    app = Flask(__name__, template_folder='../template', static_folder='../static/')
    app.config['SECRET_KEY'] = 'super secret key!'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Donors.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Admin

    create_database(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Admin.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app


def create_database(app):
    if not path.exists('template/' + DB_NAME):
        db.create_all(app=app)
        print('Create Database')
