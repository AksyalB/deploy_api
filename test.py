from flask import Flask
from control import controlServo
from schedule import sche, getSche
from register import register
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

#dynamic route

@app.route('/controlServo', methods=['POST'])
def servo_route():
    return controlServo() 

@app.route('/scheduleAlarm', methods=['POST'])
def schedule_route():
    return sche() 

@app.route('/getscheduleAlarm', methods=['GET'])
def get_schedule_route():
    return getSche() 

@app.route('/postregister', methods=['POST'])
def postRegister():
    return register() 

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))