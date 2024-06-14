from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

mysql = MySQL()
# Konfigurasi koneksi MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'api_android'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

def updateUsername():
    data = request.get_json()
    username = data['username']
    new_username = data['new_username']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
         # Periksa apakah pengguna dengan username tertentu ada
        cursor.execute("SELECT * FROM reguster WHERE username = %s", (username,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'username tidak terdaftar'
            }
            return jsonify(response)
        else:
            cursor.execute("UPDATE reguster SET `username` = '" + new_username + "' WHERE `username` = '" + username + "'")
            conn.commit()
            conn.close()

            response = {
            'status': 'success',
            'message': 'Data pengguna berhasil diperbarui',
            'new_username': new_username
            }
            return jsonify(response)
        
    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat memperbarui data pengguna',
            'error': str(e)
        }
        return jsonify(response)
    
def updateUserPassword():
    data = request.get_json()
    username = data['username']
    new_password = data['new_password']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
         # Periksa apakah pengguna dengan username tertentu ada
        cursor.execute("SELECT * FROM reguster WHERE username = %s", (username,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'username tidak terdaftar'
            }
            return jsonify(response)
        else:
            cursor.execute("UPDATE reguster SET `password` = '" + new_password + "' WHERE `username` = '" + username + "'")
            conn.commit()
            conn.close()

            response = {
            'status': 'success',
            'message': 'Data pengguna berhasil diperbarui',
            'new_password': new_password
            }
            return jsonify(response)
        
    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat memperbarui data pengguna',
            'error': str(e)
        }
        return jsonify(response)