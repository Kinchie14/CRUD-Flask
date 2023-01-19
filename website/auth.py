from flask import Blueprint, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired

auth = Blueprint("auth", __name__)


class SignupForm(FlaskForm):
    name = StringField("Input your name", validators = [DataRequired()])
    age = IntegerField("Input your age", validators = [DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password1 = PasswordField("Password", validators =[DataRequired()])
    password2 = PasswordField("Confirm your password", validators =[DataRequired()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators =[DataRequired()])
    submit = SubmitField("Login") 

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form= form)



@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    
    form = SignupForm()
    return render_template("sign-up.html", form=form)



@auth.route('/logout')
def logout():
    return render_template("logout.html")




