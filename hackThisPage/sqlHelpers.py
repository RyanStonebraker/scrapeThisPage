import sys
import pymysql

def retrieveEntries(database='catdb', table='cats', columns='*', where=''):
    host='localhost'
    user = 'root'
    password = ''

    try:
        mysqlConnection = pymysql.connect(host=host,user=user,password=password,db=database, use_unicode=True, charset='utf8')
    except Exception as e:
        sys.exit('error',e)

    mysqlCursor = mysqlConnection.cursor()
    query = "SELECT {columns} FROM {table} {where}".format(columns=columns, table=table, where=where)
    for singleQuery in query.split(';'):
        if "drop" not in singleQuery.lower() and singleQuery.strip():
            mysqlCursor.execute(singleQuery)

    mysqlConnection.commit()
    return mysqlCursor.fetchall()

def retrieveCats(catName=""):
    where = "WHERE name LIKE '%" + catName + "%'" if catName else ""
    return retrieveEntries('catdb', 'cats', '*', where)
