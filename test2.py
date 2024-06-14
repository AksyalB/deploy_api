from flask import Flask, Response
from control import button_press, getRaspiTekan
from schedule import sche, getSche, updateSwitch, getRaspiAlarm
from register import register
from updateuser import updateUsername, updateUserPassword
from login import login
from user import getUser
from testcamera import generate_frames
import os

app = Flask(__name__)

@app.route('/scheduleAlarm', methods=['POST'])
def schedule_route():
    return sche() 

@app.route('/getscheduleAlarm', methods=['GET'])
def get_schedule_route():
    return getSche() 

@app.route('/postregister', methods=['POST'])
def postRegister():
    return register() 

@app.route('/login', methods=['POST'])
def postLogin():
    return login() 

@app.route('/getUser', methods=['GET'])
def userGet():
    return getUser()

@app.route('/changeusername', methods=['POST'])
def changeuser():
    return updateUsername()

@app.route('/changepassword', methods=['POST'])
def changepass():
    return updateUserPassword()

@app.route('/updateswitch', methods=['POST'])
def alarmswitch():
    return updateSwitch()

# CONNECT TO RASPBERRY

@app.route('/butpress', methods=['POST'])
def servo_terbuka():
    return button_press()

@app.route('/getcontraspi', methods=['GET'])
def buat_raspi():
    return getRaspiTekan()

@app.route('/getscheduledata', methods=['GET'])
def schedule_raspi():
    return getRaspiAlarm()

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))