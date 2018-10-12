from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import make_response
from hackThisPage import app

from sqlHelpers import *

import random

@app.route("/")
def index():
    cats = retrieveCats()
    return render_template("index.html", cats=cats, frontpage=True)

@app.route("/search")
def search():
    catName = request.args.get('catName')
    cats = retrieveCats(catName)
    return render_template("index.html", cats=cats)

@app.route("/login", methods=['GET', 'POST'])
def login():
    errorMessage = None
    if request.method == 'POST':
        usersCreds = retrieveEntries('users', 'credentials', '*')
        for userCreds in usersCreds:
            if request.form['username'] == userCreds[0] and request.form['password'] == userCreds[1]:
                response = make_response(redirect(url_for('index')))
                response.set_cookie('COOKIE', str(int(random.random() * 100)))
                return response
        errorMessage="ERROR! The username or password is not valid."
    return render_template("login.html", loginpage=True, errorMessage=errorMessage)
