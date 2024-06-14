import cv2
import imagezmq
import socket

# Setup image sender
sender = imagezmq.ImageSender(connect_to='tcp://192.168.1.9:5555')
rpiName = socket.gethostname()

frameW = 640
frameH = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameW)
cap.set(4, frameH)

while True:
    success, img = cap.read()
    # Send image to the server and receive the response
    reply_msg = sender.send_image(rpiName, img)

    # The reply_msg is the predictions text received, decode it
    predictions_text = reply_msg.decode('utf-8')

    # Now you can use the predictions_text, for example, print it
    print(predictions_text)


    if cv2.waitKey(1) & 0xff == ord('q'):
        break
