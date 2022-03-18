import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****',
    database = 'BOOKS'
)
cursor = mydb.cursor()
cursor.execute("CREATE TABLE NAMES(title varchar(200),author varchar(20),price varchar(200))")
cursor.execute("SHOW TABLES")
for tb in cursor:
    print(tb)
