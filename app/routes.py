from flask import(Flask,render_template,redirect,request,flash,url_for,session,logging)
from passlib.hash import sha256_crypt
from app import app, db
from app.models import User
from app.validators import User

@app.rooute("/register", methods=['GET,POST'])
def register():
    form = User(request.form)
    if request.method == "POST" and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt(str(form.password.data))
        #Insert into database
        user = User(firstname = firstname, lastname = lastname, username = username, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        flash("User Added","success")
    return render_template("register.html", form=form)


