from flask import Flask, request
from db_connect import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Kapni backend is running"

@app.route('/login', methods=['GET','POST'])
def login():

    # If opened in browser
    if request.method == 'GET':
        return "Login API is ready. Use POST to login."

    # If called from Thunder/Postman
    data = request.json
    username = data['username']
    password = data['password']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.callproc('sp_login', (username, password))
    result = cursor.fetchall()

    return {"message": result[0][0]}

app.run(debug=True)
# register api coming soon
