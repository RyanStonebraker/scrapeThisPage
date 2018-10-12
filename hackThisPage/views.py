from flask import render_template
from flask import request
from flask import redirect
from hackThisPage import app

import sys

def retrieveCats(catName=""):
    import pymysql
    host='localhost'
    user = 'root'
    password = ''
    database = 'catdb'

    try:
        mysqlConnection = pymysql.connect(host=host,user=user,password=password,db=database, use_unicode=True, charset='utf8')
    except Exception as e:
        sys.exit('error',e)

    mysqlCursor = mysqlConnection.cursor()
    if (not catName):
        mysqlCursor.execute("SELECT * FROM cats")
    else:
        query = "SELECT * FROM cats WHERE name LIKE '%" + catName + "%'"
        mysqlCursor.execute(query)
    cats = mysqlCursor.fetchall()

    return cats

@app.route("/")
def index():
    cats = retrieveCats()
    return render_template("index.html", cats=cats)

@app.route("/search")
def search():
    catName = request.args.get('catName')
    cats = retrieveCats(catName)
    return render_template("index.html", cats=cats)
