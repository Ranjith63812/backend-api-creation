import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='your_database_name'
    )
    return connection
