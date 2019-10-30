import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = 'Welearneveryday'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql://root:@localhost/login' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False