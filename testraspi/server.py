from socket import *
from servomotor import setup, ServoUp, ServoDown, close
from time import sleep

setup()

ctrCmd = ['Up', 'Down']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    try:
        while True:
            data = tcpCliSock.recv(BUFSIZE).decode()  # Decode received bytes to string
            if not data:
                break
            if data == ctrCmd[0]:
                ServoUp()  # Corrected function call
                print('Increase:', ServoUp.cur_X)  # Corrected variable reference
            if data == ctrCmd[1]:
                ServoDown()  # Corrected function call
                print('Decrease:', ServoDown.cur_X)  # Corrected variable reference
    except KeyboardInterrupt:
        close()  # Corrected function call
        tcpCliSock.close()
        tcpSerSock.close()
        break  # Exit the loop