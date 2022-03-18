import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****',
    database = 'BOOKS'
)
cursor = mydb.cursor()
while True:
    x=input("want to enter data yes/no: ")
    if x=='yes':
        title=input("Enter book name: ")
        author=input("Enter author name: ")
        price=input("Enter price of book: ")
        sql = "INSERT INTO NAMES(title,author, price) VALUES(%s, %s, %s)"
        val = (title, author, price)
        try:
            cursor.execute(sql, val)
            mydb.commit()
        except:
            mydb.rollback()
        print(cursor.rowcount, "record inserted!")
        mydb.close()

    else:
        break
