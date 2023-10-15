# a python pakage for website folder
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #for database
from os import path # to check if the path of the database exixts
from flask_login import LoginManager

db = SQLAlchemy() #creating database(present in models.py)
DB_NAME = "database.db"


def create_app(): 
    app = Flask(__name__) #__name__ represents the name of the file 
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs' #encrypt the cookies and session data related to website 
    #( hjshjhdjah kjshkjdhjs secret key to the app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #F-strings provide a way to embed expressions inside
    #string literals, using a minimal syntax 
    # SQLALCHEMY_DATABASE_URI - instructs where to create the database
    db.init_app(app) 

    from .views import views #imporing the blueprint which is named as views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #registering blueprint with no prefix
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note #

    create_database(app) #to check if the database already exists and if does not, it is going to create it

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app 


def create_database(app):
    if not path.exists('website/' + DB_NAME): # if the path does not exists it will create the db
        db.create_all(app=app) 
        print('Created Database!')