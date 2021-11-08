import mysql.connector
def getdbconnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dileep@369874",
        database="casestudy"
    )
    return mydb
