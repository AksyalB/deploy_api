import cv2
import imagezmq
from ultralytics import YOLO  # Import YOLO dari Ultralytics

# Load the YOLOv8 model
model = YOLO('best.pt')  # Ganti 'yolov8n.pt' dengan lokasi model yang tepat

# Initialize image receiver
image_hub = imagezmq.ImageHub()

while True:
    # Receive image from Raspberry Pi
    rpi_name, image = image_hub.recv_image()

    # Run YOLOv8 inference on the received image
    results = model(image)

    # Visualize the results on the image
    annotated_image = results[0].plot()

    # for result in results:
    #     if result.boxes:
    #         box = result.boxes[0]
    #         class_id = int(box.cls)
    #         object_name = model.names[class_id]
    #         print(object_name)

    # Display the annotated image
    cv2.imshow(rpi_name, annotated_image)  # 1 window for each RPi

    # Send a reply to the Raspberry Pi
    image_hub.send_reply(b'Kirim balik ke raspi')

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()