import mysql.connector

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)
if db.is_connected():
    print("berhasil")
