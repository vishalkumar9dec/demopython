import mysql.connector

mydb = mysql.connector.connect(host ="localhost",user="root",passwd='root123',database="pytestdb")

mycursor = mydb.cursor()

mycursor.execute("select * from students")

for i in mycursor:
    print(i)
