from flask import(Flask,render_template,redirect,request,flash,url_for,session,logging)
from passlib.hash import sha256_crypt
from app import app, db
from app.models import User
from app.validators import Users
from app.email import *



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/register", methods=['GET','POST'])
def register():
    form = Users(request.form)
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        email_check = User.query.filter_by(email=email).first()

        if email_check is not None:
            return flash("User already exist","danger")

        if check_email_validation(email):
            password = sha256_crypt.encrypt(str(form.password.data))
            #Insert into database
            user = User(firstname = firstname, lastname = lastname, username = username, email = email, password = password, activate =False)
            send_confirmation_mail(email, username)
        else:
            return flash("The email you entered is invalid","danger")
        db.session.add(user)
        db.session.commit()
        #flash("User Added","success")
    return render_template("register.html", form = form)



@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
       username = request.form['username']  
       password_candidate = request.form['password']
       result = User.query.filter_by(username= username).first()

       if result is not None :
            password  = result.password
            if sha256_crypt.verify(password_candidate,password):
                session['logged_in'] = True
                session['username'] = username

                if result.activate is False:
    		        return render_template('unconfirmed.html')
                else:

                flash("You are currently logged in success",'success')
                return redirect(url_for("dashboard"))

            else:
                flash("Invalid login credentials",'danger')
                return render_template("login.html")

       else:
            error = "User not found"
            return render_template("login.html", error = error)
    return render_template("login.html")



@app.route('/confirm/<token>')
def confirm_email(token):
	try:
		data = confirm_token(token)
	except:
		return 'token expired'

	user = User.query.filter_by(username=data['username']).first()
	if user:
		user.activate=True
		db.session.add(user)
		db.session.commit()

	return 'ok'


@app.route('/resend')
def resend_confirmation():
	send_confirmation_mail(session['email'], session['username'])
	return 'ok'


@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	# clear browser cache
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r
