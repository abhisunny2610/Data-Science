# Q1. Write a Python program to create a MySQL database and a table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="abhishek",
    password="abhishek123@"
)

if mydb.is_connected():
    print("Connection Successfull")
else:
    print("Connectivity Issued")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists practice_database")

mycursor.execute(
    "CREATE TABLE if not exists practice_database.practice_table(c1 INT, c2 VARCHAR(30), c3 VARCHAR(30))")


# Q2. Write a Python program to insert data into a MySQL table.

mycursor.execute(
    "INSERT INTO practice_database.practice_table values(101, 'Abhishek', 'Singh')")

# Q3. Write a Python program to create an index on a MySQL table.

# mycursor.execute("CREATE INDEX if not exists c3 ON practice_database.practice_table (c3)")

# Q4. Write a Python program to join two tables in MySQL.

mycursor.execute(
    "CREATE TABLE if not exists practice_database.practice_table2(c4 INT, c5 VARCHAR(30), c6 VARCHAR(30))")

# mycursor.execute(
#     "SELECT * FROM practice_database.practice_table JOIN practice_database.practice_table2 ON practice_table.c2=practice_table2.c5")

mycursor.execute("SELECT * FROM practice_database.practice_table")

for i in mycursor.fetchall():
    print(i)

mydb.close()
