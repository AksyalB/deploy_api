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

def getUser():
    user_id = request.args.get('id')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    if user_id is None:
        query = "SELECT * FROM reguster ORDER BY id DESC LIMIT 1"
    else:
        query = "SELECT * FROM reguster WHERE id = '" + user_id + "'"
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'email': row[1],
                'nama': row[2],
                'username': row[3],
                'password': row[4]
            }
            results.append(result)

        return jsonify(results)

    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat mengambil data',
            'error': str(e)
        }
        return jsonify(response)

