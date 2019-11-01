from flask import(Flask,render_template,redirect,request,flash,url_for,session,logging)
from passlib.hash import sha256_crypt
from app import app, db
from app.models import User
from app.validators import Users

@app.route("/register", methods=['GET','POST'])
def register():
    form = Users(request.form)
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        #Insert into database
        user = User(firstname = firstname, lastname = lastname, username = username, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        flash("User Added","success")
    return render_template("register.html", form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
       username = request.form['username']  
       password_candidate = request.form['password']
       result = User.query.filter_by(username= username).first()
       if result :
            password  = result.password
            if sha256_crypt.verify(password_candidate,password):
                session['logged_in'] = True
                session['username'] = username
                flash("You are currently logged in success",'success')
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid credentials",'danger')
                return render_template("login.html")
       else:
            error = "User not found"
            return render_template("login.html", error = error)
    return render_template("login.html")
