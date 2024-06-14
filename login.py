from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# Konfigurasi koneksi MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'api_android'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM reguster WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            id = result[0]
            nama = result[2]

            response = {
                'status': 'success',
                'message': 'Login berhasil',
                'username': username,
                'nama': nama,
                'id': id
            }

            return jsonify(response)
        else:
            conn.close()
            response = {
                'status': 'error',
                'message': 'Username atau Password Salah'
            }
            return jsonify(response)
    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat login',
            'error': str(e)
        }
        return jsonify(response)
    
