from wtforms import Form, StringField, TextAreaField,PasswordField,SelectField, validators

class Users(Form):
    firstname = StringField(u'Firstname', validators=[validators.input_required(),validators.Length(min=3, max=250)])
    lastname = StringField(u'Lastname', validators=[validators.input_required(),validators.Length(min=3, max=250)])
    username = StringField(u'Username', validators=[validators.input_required(),validators.Length(min=3, max=250)])
    email = StringField(u'Email', validators=[validators.input_required(),validators.Length(min=3, max=250)])
    password = PasswordField('Password',[validators.DataRequired(),
    validators.EqualTo('confirm',message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')