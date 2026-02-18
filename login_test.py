import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Ranjith@5',
    database='kapni'
)

cursor = conn.cursor()

username = "Ranjith"
password = "ranjith123"

cursor.callproc('sp_login', (username, password))

for result in cursor.fetchall():
    print(result)

conn.close()
