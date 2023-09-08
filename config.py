import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'op43unkutcgn348gh34jilkkerntrafoijc48ghenjkmy23907ztrhn72iu'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    MAIL_SERVER = 'proxymail'
    MAIL_PORT = 25
    MAIL_USE_TLS = 0
    MAIL_USERNAME =
    MAIL_PASSWORD = ''
    ADMINS =
    REQUEST_RECIPIENT = 
    CONTACT_RECIPIENT =
    
