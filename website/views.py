from flask import Blueprint, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

views = Blueprint("views", __name__)

class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators = [DataRequired()])
    submit = SubmitField("Submit")


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/name', methods = ['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('The form has been submitted successfully', category ='success')

    return render_template("name.html",
        name = name,
        form = form)



