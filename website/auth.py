from flask import Blueprint, render_template, url_for, redirect

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return 'Tanginamo dis is login'