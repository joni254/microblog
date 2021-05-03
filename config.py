import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a very long key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://mwangi:.D3v3l0p3r!@localhost/myblog'
    DEBUG = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int( os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['john@citorium.com']
         
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
