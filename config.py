import os

basedir = os.path.abspath(os.path.dirname(__file__))

''' SQLALCHEMY_DATABASE_URI ='postgresql://mwangi:.D3v3l0p3r!@localhost/blog'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')   
      '''
class Config(object):
    SECRET_KEY = os.environ.get ('SECRET_KEY') or 'A very very long key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://mwangi:.D3v3l0p3r!@localhost/blog'
     
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    