import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='****',
    database='BOOKS'
)
cursor = mydb.cursor()
name = input("enter name:")
cursor.execute("SELECT title,author,price from NAMES WHERE title = '"+name+"'")
myresult = cursor.fetchone()
for y in myresult:
    print(y)
cost = 0
while True:
    copies = int(input("NO. OF COPIES:"))
    confirmation = input("Add more books?Y/N")
    n = int(myresult[2])
    if confirmation == 'N':
        cost = copies * n
        print("Total cost of the books: %d" % (cost))
        break
    elif confirmation == 'Y':
        pass
