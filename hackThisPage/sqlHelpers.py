import sys
import pymysql
import random

def executeQuery(database, query):
    host='localhost'
    user = 'root'
    password = ''

    try:
        mysqlConnection = pymysql.connect(host=host,user=user,password=password,db=database, use_unicode=True, charset='utf8')
    except Exception as e:
        sys.exit('error', e)

    mysqlCursor = mysqlConnection.cursor()

    for singleQuery in query.split(';'):
        if "drop" not in singleQuery.lower() and singleQuery.strip():
            mysqlCursor.execute(singleQuery)

    mysqlConnection.commit()
    return mysqlCursor.fetchall()


def retrieveEntries(database='catdb', table='cats', columns='*', where=''):
    query = "SELECT {columns} FROM {table} {where}".format(columns=columns, table=table, where=where)
    return executeQuery(database, query)

def retrieveCats(catName=""):
    where = "WHERE name LIKE '%" + catName + "%'" if catName else ""
    return retrieveEntries('catdb', 'cats', '*', where)

def addCat(catName, catPrice="", catDescription="", catPicture=""):
    query = """
        INSERT INTO cats (name, price, description, picture)
        VALUES ("{catName}", {catPrice}, "{catDescription}", "{catPicture}")
    """.format(catName=catName, catPrice=catPrice, catDescription=catDescription, catPicture=catPicture)

    print("QUERY:", query)
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
