import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a very long key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://mwangi:.D3v3l0p3r!@localhost/myblog'
    DEBUG = True
     
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
