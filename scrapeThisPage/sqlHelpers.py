import sys
import pymysql
import random
import re

from scrapeThisPage import app


def executeQuery(database, query):
    host = app.config["HOST"]
    user = app.config["SQL_USER"]
    password = app.config["SQL_PASSWORD"]

    try:
        mysqlConnection = pymysql.connect(host=host, user=user, password=password, db=database, use_unicode=True, charset='utf8')
    except Exception as e:
        sys.exit(e)

    mysqlCursor = mysqlConnection.cursor()

    mysqlCursor.execute(query)

    mysqlConnection.commit()
    return mysqlCursor.fetchall()


def retrieveEntries(database='catdb', table='cats', columns='*', where=''):
    query = "SELECT {columns} FROM {table} {where}".format(columns=columns, table=table, where=where)
    return executeQuery(database, query)


def retrieveCats(catName=""):
    catName = catName.replace(";", "").replace("'", "").replace('"', "")[:20]
    where = "WHERE name LIKE '%" + catName + "%'" if catName else ""
    return retrieveEntries('catdb', 'cats', 'picture, price, description, name', where)


def addCat(catName, catPrice="", catDescription="", catPicture=""):
    query = """
        INSERT INTO cats (name, price, description, picture)
        VALUES ("{catName}", {catPrice}, "{catDescription}", "{catPicture}")
    """.format(catName=catName, catPrice=catPrice, catDescription=catDescription, catPicture=catPicture)

    executeQuery('catdb', query)


def getUserSessionId(username):
    query = """
        SELECT sess_id
        FROM credentials
        WHERE username="{username}"
    """.format(username=username)

    return executeQuery('users', query)[0][0]


def updateUserSessionId(username):
    sessionId = str(int(random.random() * 100000))

    query = """
        UPDATE credentials
        SET sess_id ="{sessionId}"
        WHERE username="{username}"
    """.format(sessionId=sessionId, username=username)

    executeQuery('users', query)

    return sessionId
