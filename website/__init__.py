from flask import Flask

def create_app():
    "function to create and intialize app"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hard to guess'  #secures the cookies and session date

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app