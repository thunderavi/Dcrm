import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Hittu@09',

	)

cursorObject =dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")