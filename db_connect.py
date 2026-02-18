import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ranjith@5',
        database='kapni'
    )
    return connection
