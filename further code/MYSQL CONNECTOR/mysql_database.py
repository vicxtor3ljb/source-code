import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="vicxtor3",
	password="@25Julio1985"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
