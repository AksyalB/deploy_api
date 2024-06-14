import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.tcp.ap.ngrok.io", 12819))

print(client.recv(1024).decode())
client.send("halo server".encode())
