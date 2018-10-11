from flask import render_template
from flask import request
from flask import redirect
from hackThisPage import app

@app.route("/")
def index():
    return render_template("index.html")
