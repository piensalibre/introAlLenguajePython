import os

class Config(object):
    SECRET_KEY = "dsfsdfsdfs"

class DevelopmentConfig(Config):
    DEBUG =True
    SQLALCHEMY_DATABASE_URI =  'mysql://piensa:PIENSAlibre3443.,@localhost/tutocf'
    SQLALCHEMY_TRACK_MODIFICATIONS =False