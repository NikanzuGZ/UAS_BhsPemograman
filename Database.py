import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "uas_bhspemograman"
)

cursor = db.cursor()
sql = "INSERT INTO peserta (name, address) VALUES (%s, %s)"
values = [
    ("Daven", "Kalimantan")
    ("Exalta", "Tangerang")
    ("Dika", "Tangerang")
    ("Lutfi", "Tangerang")
]
