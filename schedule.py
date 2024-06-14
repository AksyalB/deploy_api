
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

def sche():
    data = request.get_json()
    userId = data['userId']
    waktu = data['waktu']
    jns_hewan = data['jns_hewan']
    jns_tank = data['jns_tank']
    jmlh_pakan = data['jmlh_pakan']
    kondisi_switch = data['kondisi_switch'] 

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO schedule_alarm (userId, waktu, jns_hewan, jns_tank, jmlh_pakan, kondisi_switch) VALUES (%s, %s, %s, %s, %s, %s)", (userId, waktu, jns_hewan, jns_tank, jmlh_pakan, kondisi_switch))
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


def getSche():
    sche_id = request.args.get('userId')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    if sche_id is None:
        query = "SELECT * FROM schedule_alarm"
    else:
        query = "SELECT * FROM schedule_alarm WHERE userId = '" + sche_id + "'"
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'waktu': row[2],
                'jns_hewan': row[3],
                'jns_tank': row[4],
                'jmlh_pakan': row[5]
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
    
def updateSwitch():
    data = request.get_json()
    id= data["id"]
    kondisi_switch = data['kondisi_switch']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        # Periksa apakah pengguna dengan userId tertentu ada
        cursor.execute("SELECT * FROM schedule_alarm WHERE id = %s", (id,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'userId tidak terdaftar'
            }
            return jsonify(response), 404

        # Toggle switch
        new_switch_status = 1 if kondisi_switch else 0
        cursor.execute("UPDATE schedule_alarm SET kondisi_switch = %s WHERE id = %s LIMIT 1", (new_switch_status, id))
        
        conn.commit()
        conn.close()
        
        response = {
            'status': 'success',
            'message': 'Status switch berhasil diperbarui',
            'kondisi_switch': new_switch_status
        }
        return jsonify(response), 200

    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat memperbarui data pengguna',
            'error': str(e)
        }
        return jsonify(response), 500

def getRaspiAlarm():
    getdata = request.args.get('userId')

    conn = mysql.connect()
    cursor = conn.cursor()

    if getdata is None:
        query = "SELECT * FROM schedule_alarm ORDER BY userId DESC LIMIT 1"
    else:
        query = "SELECT * FROM schedule_alarm WHERE userId = '" + getdata + "'"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'waktu': row[2],
                'jns_hewan': row[3],
                'jns_tank': row[4],
                'jmlh_pakan': row[5],
                'kondisi_switch': row[6]
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




