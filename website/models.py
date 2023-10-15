from . import db #from this package we can access anything in __init__.py
from flask_login import UserMixin # usermixin - to check if login credentials provide is correct or not
from sqlalchemy.sql import func # to automatically store the date and time (func) and adding to the database which is handled by 
#sql alchemy


class Note(db.Model): #all the notes need to satisfy the below condition
    id = db.Column(db.Integer, primary_key=True) # each note should have a unique id
    data = db.Column(db.String(10000)) # to store the text
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # to store the timezone information 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # associating different users to their information
# we must pass a valid id of an existing user to this column when we create a note(we have one user with many notes)
#(user.id is in lowercase)

class User(db.Model, UserMixin): #all the user need to satisfy the below condition
    id = db.Column(db.Integer, primary_key=True)  #primary key(integer) - to uniquely identify each user
    email = db.Column(db.String(150), unique=True) # unique email id
    password = db.Column(db.String(150)) 
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # tells flask and sqlalchemy to add notes into the user's account
    #(Notes - " N " is in uppercase)
    
    
  
