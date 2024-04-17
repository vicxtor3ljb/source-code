import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="vicxtor3",
	password="@25Julio1985",
	database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
