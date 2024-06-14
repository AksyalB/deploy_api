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
        
def button_press():
    data = request.get_json()
    userId = data['userId']
    jns_tank = data['jenis_tank']
    jns_hewan = data['jenis_hewan']
    button = data['buka_servo']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO control_manual (userId, jenis_tank, jenis_hewan, buka_servo) VALUES (%s, %s, %s, %s)", (userId, jns_tank, jns_hewan, button))
        conn.commit()
        conn.close()

        response = {
            'status': 'success',
            'message': 'data berhasil dimasukan'
        }
        
        return jsonify(response)
    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat inout data',
            'error': str(e)
        }
        return jsonify(response)


#COBA COBA SAMBUNGIN RASPI 

def getRaspiTekan():
    getdata = request.args.get('userId')

    conn = mysql.connect()
    cursor = conn.cursor()

    if getdata is None:
        # query = "SELECT * FROM control_manual ORDER BY id DESC LIMIT 1"
        query = "SELECT * FROM control_manual ORDER BY id DESC LIMIT 1"
    else:
        query = "SELECT * FROM control_manual WHERE userId = '" + getdata + "'"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'jenis_hewan': row[3],
                'jenis_tank': row[2],
                'buka_servo': row[4]
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


