
from flask import Flask, request, jsonify, Response
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

mysql = MySQL()
# Konfigurasi koneksi MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'api_android'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/scheduleAlarm', methods=['POST'])
def schedule_route():
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
    

@app.route('/getscheduleAlarm', methods=['GET'])
def get_schedule_route():
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
    

@app.route('/deletescheduleAlarm', methods=['DELETE'])
def deleteschedulealarm():
    sche_user_id = request.args.get('userId')
    sche_id = request.args.get('id')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()


    try:
        cursor.execute("DELETE FROM schedule_alarm WHERE userId = %s AND id = %s " , (sche_user_id, sche_id,))
        conn.commit()

        if cursor.rowcount == 0:
            response = {
                'status': 'error',
                'message': f'No record found with id {id}'
            }
            return jsonify(response), 404

        response = {
            'status': 'success',
            'message': f'Record with id {id} successfully deleted'
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat menghapus data',
            'error': str(e)
        }
        return jsonify(response), 500

@app.route('/postregister', methods=['POST'])
def postRegister():
    data = request.get_json()
    email = data['email']
    nama = data['nama']
    username = data['username']
    password = data['password']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM reguster WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'Username sudah terdaftar'
            }
            return jsonify(response)

        cursor.execute("INSERT INTO reguster (email, nama, username, password) VALUES (%s, %s, %s, %s)", (email, nama, username, password))
        conn.commit()
        conn.close()

        response = {
            'status': 'success',
            'message': 'Akun berhasil dibuat'
        }

        return jsonify(response)
    except Exception as e:
        conn.rollback()
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat membuat akun',
            'error': str(e)
        }
        return jsonify(response)

@app.route('/login', methods=['POST'])
def postLogin():
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
    
@app.route('/getUser', methods=['GET'])
def userGet():
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
    
@app.route('/changeusername', methods=['POST'])
def changeuser():
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
    
@app.route('/changepassword', methods=['POST'])
def changepass():
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
    
@app.route('/updateswitch', methods=['POST'])
def alarmswitch():
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
    
# CONNECT TO RASPBERRY

@app.route('/butpress', methods=['POST'])
def servo_terbuka():
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
    
@app.route('/getdatamanual', methods=['GET'])
def GetManual():
    sche_id = request.args.get('userId')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    if sche_id is None:
        query = "SELECT * FROM control_manual ORDER BY id DESC LIMIT 1"
    else:
        query = "SELECT * FROM control_manual WHERE userId = %s ORDER BY id DESC LIMIT 1"
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'jenis_tank': row[2],
                'jenis_hewan': row[3],
                'jumlah_pakan': row[5]
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

@app.route('/getcontraspi', methods=['GET'])
def buat_raspi():
    getdata = request.args.get('userId')

    conn = mysql.connect()
    cursor = conn.cursor()

    if getdata is None:
        query = "SELECT * FROM control_manual ORDER BY id DESC LIMIT 1"
    else:
        query = "SELECT * FROM control_manual WHERE userId = %s ORDER BY id DESC LIMIT 1"

    try:
        if getdata is None:
            cursor.execute(query)
        else:
            cursor.execute(query, (getdata,))
        
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
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat mengambil data',
            'error': str(e)
        }
        return jsonify(response)
    
@app.route('/getscheduledata', methods=['GET'])
def dataloadcell_raspi():
    getdata = request.args.get('userId')

    conn = mysql.connect()
    cursor = conn.cursor()

    if getdata is None:
        query = "SELECT * FROM schedule_alarm ORDER BY id DESC LIMIT 1"
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
    
@app.route('/postdataloadcell', methods=['POST'])
def schedule_raspi():
    data = request.get_json()
    id = data["id"]
    berat = data['berat']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        # Periksa apakah id sudah ada
        cursor.execute("SELECT * FROM schedule_alarm WHERE id = %s", (id,))
        result = cursor.fetchone()

        if not result:
            # Jika id tidak ditemukan, masukkan data baru
            cursor.execute("INSERT INTO schedule_alarm (id, berat) VALUES (%s, %s)", (id, berat))
        else:
            # Jika id ditemukan, perbarui data
            cursor.execute("UPDATE schedule_alarm SET berat = %s WHERE id = %s", (berat, id))
        
        conn.commit()
        conn.close()
        
        response = {
            'status': 'success',
            'message': 'Data load cell berhasil diperbarui'
        }
        return jsonify(response), 200

    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat memperbarui data',
            'error': str(e)
        }
        return jsonify(response), 500
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))