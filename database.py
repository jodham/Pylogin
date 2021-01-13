import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase1"
)
mycur = mydb.cursor()
#mycur.execute("CREATE DATABASE mydatabase1")
#mycur.execute("CREATE TABLE logindetails(id Integer PRIMARY KEY AUTO_INCREMENT,username VARCHAR(255),password VARCHAR(255))")
