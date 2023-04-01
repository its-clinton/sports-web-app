from wtforms import Form, PasswordField, validators, BooleanField, IntegerField, SelectField, TextAreaField, HiddenField, StringField

from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField('Email', validators = [validators.Length(min=6, max=40), validators.DataRequired(message="Please fill in your email.")])
    password = PasswordField('password', validators = [validators.DataRequired(message="Please fill in your password.")])
    
class RegistrationForm(Form):
    # first_name = StringField('First Name', validators = [validators.Length(min=3,max=30), validators.DataRequired(message="Please fill in your name.")])
    # last_name = StringField('Last Name', validators = [validators.Length(min=3,max=30), validators.DataRequired(message="Please fill in your name.")])
    name = StringField('Username', validators = [validators.Length(min=4, max=25), validators.DataRequired(message="Please fill in your username.")])
    # phone_number = IntegerField('Phone', validators= [validators.DataRequired(message="Please fill in your phone number.")])
    email = StringField('Email', validators = [validators.DataRequired(message="Please fill in your email.")])
    password = PasswordField('Password', validators = [validators.DataRequired(message="Please fill in your password."), validators.EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField('Confirm Password', validators=[validators.DataRequired(message="Please fill in your password.")])