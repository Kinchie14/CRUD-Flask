from flask import Blueprint, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/name')
def name():
    return render_template("name.html")

class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators = [DataRequired()])
    submit = SubmitField("Submit")

