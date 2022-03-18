import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='Prasu_26'
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE BOOKS")
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)
