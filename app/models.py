from app import db

class User(db.model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(250),index=True, nullable=False)
    lastname = db.Column(db.String(250),index=True, nullable=False)
    username = db.Column(db.String(250),index=True, nullable=False)
    email = db.Column(db.String(250), index=True, nullable=False)
    password = db.Column(db.String(250), index=True,nullable=False)