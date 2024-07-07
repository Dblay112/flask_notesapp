from flask import Flask

def create_app():
    "function to create and intialize app"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hard to guess'  #secures the cookies and session date

    return app