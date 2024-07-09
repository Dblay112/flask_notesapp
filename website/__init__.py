from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os  # Import the os module

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    """Function to create and initialize the Flask app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hard to guess'  # Secures the cookies and session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):  # Use os.path.exists
        db.create_all(app=app)
        print('Database Created Successfully')
