from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(100))
    comments = db.relationship("Comment")
    created_at = db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self, username,password,email):
        self.username = username
        self.password = self.__createPassword(password)
        self.email = email

    def __createPassword(self,password):
        return generate_password_hash(password)

    def verifyPassword(self,password):
        return check_password_hash(self.password,password)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)