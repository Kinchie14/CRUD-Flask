from flask import Blueprint, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired
from . import db
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


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
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", form= form, user=current_user)



@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit(): 
        name = form.name.data
        age = form.age.data
        email = form.email.data
        password1 = form.password1.data
        password2 = form.password2.data


        user = User.query.filter_by(email = email).first()
        if user:
            flash('The user has already been created', category='error')
            return redirect(url_for('auth.sign_up'))
        elif len(name) < 2:
            flash('The name should be greater than 2 characters', category='error')
            return redirect(url_for('auth.sign_up'))
        elif age < 12:
            flash("You're still a kid", category='error')
            return redirect(url_for('auth.sign_up'))
        elif len(email) < 3:
            flash('Email should be greater than 3 characters', category='error')
            return redirect(url_for('auth.sign_up'))
        elif password1 != password2:
            flash('Password should be the same', category='error')
            return redirect(url_for('auth.sign_up'))
        else:
            new_user = User( name = name, age = age, email = email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('New user has been created', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign-up.html", form=form, user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))




