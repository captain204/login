import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'Just-another-random-thought'
    SECURITY_PASSWORD_SALT = 'my_password_salt'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'login.db')
    MAIL_SERVER = 'smtp.gmail.com:587'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

