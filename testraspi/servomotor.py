# import RPi.GPIO as GPIO
# import time
# cur_X = 0 #initial value of servo motor
# def setup():
#         GPIO.setmode(GPIO.BOARD)
#         GPIO.setup(3,GPIO.OUT)
#         global servo
#         servo=GPIO.PWM(11,50)
#         servo.start(2.5)
#         servo.ChangeDutyCycle(2.5)
#         #start pwm with Duty Cycle is 2% --> Pluse with = 2%*20ms = 0.4ms
# #Create PWM on pin 11 with frequency 50Hz --> period 20ms
# def ServoUp():
#         global cur_X
#         cur_X += 2.5
#         if cur_X >12:
#                 cur_X = 12.5
#         servo.ChangeDutyCycle(cur_X)
#         time.sleep(1)
# def ServoDown():
#         global cur_X
#         cur_X -= 2.5
#         if cur_X <2.5:
#                 cur_X = 2.5
#         servo.ChangeDutyCycle(cur_X)
#         time.sleep(1)
# def close():
#         servo.stop()
# if __name__ == '__main__':
#         setup()

from gpiozero import AngularServo
from time import sleep

cur_X = 0  # initial value of servo motor
servo = None

def setup():
    global servo
    servo = AngularServo(11, min_angle=-90, max_angle=90)

def ServoUp():
    global cur_X
    cur_X += 30
    if cur_X > 90:
        cur_X = 90
    servo.angle = cur_X
    sleep(1)

def ServoDown():
    global cur_X
    cur_X -= 30
    if cur_X < -90:
        cur_X = -90
    servo.angle = cur_X
    sleep(1)

def close():
    servo.detach()

if __name__ == '__main__':
    setup()
