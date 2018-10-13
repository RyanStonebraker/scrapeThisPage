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
    username = request.cookies.get("USERNAME") if "USERNAME" in request.cookies else ""
    return render_template("index.html", cats=cats, frontpage=True, username=username)

@app.route("/search")
def search():
    catName = request.args.get('catName')
    cats = retrieveCats(catName)
    username = request.cookies.get("USERNAME") if "USERNAME" in request.cookies else ""
    return render_template("index.html", cats=cats, username=username)

@app.route("/login", methods=['GET', 'POST'])
def login():
    errorMessage = None
    if request.method == 'POST':
        usersCreds = retrieveEntries('users', 'credentials', '*')
        for userCreds in usersCreds:
            if request.form['username'] == userCreds[0] and request.form['password'] == userCreds[1]:
                simpleSessionId = updateUserSessionId(request.form['username'])
                response = make_response(redirect(url_for('index')))
                response.set_cookie('USERNAME', request.form['username'])
                response.set_cookie('SIMPLE_SESSID', simpleSessionId)
                return response
        errorMessage = "ERROR! The username or password is not valid."
    return render_template("login.html", loginpage=True, errorMessage=errorMessage)

@app.route("/logout", methods=['GET'])
def logout():
    if "USERNAME" in request.cookies:
        response = make_response(redirect(url_for('index')))
        response.set_cookie('USERNAME', '', expires=0)
        response.set_cookie('SIMPLE_SESSID', '', expires=0)
        return response

@app.route("/post", methods=['GET', 'POST'])
def post():
    if "USERNAME" in request.cookies and "SIMPLE_SESSID" in request.cookies:
        username = request.cookies.get("USERNAME")
        userSessId = getUserSessionId(username)
        cachedSessId = request.cookies.get("SIMPLE_SESSID")

        if userSessId == cachedSessId:
            if request.method == 'POST':
                catName = request.form['catName']
                catPrice = request.form['catPrice']
                catDescrip = request.form['catDescrip']
                catPicture = request.form['catPicture']
                addCat(catName, catPrice, catDescrip, catPicture)
            return render_template("postCat.html", authenticated=True, username=username)
    return render_template("postCat.html")
