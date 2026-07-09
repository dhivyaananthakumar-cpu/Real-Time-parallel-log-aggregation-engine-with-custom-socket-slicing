import socket
import struct

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Waiting for Logs...")

client, address = server.accept()

print("Connected :", address)

while True:

    data = client.recv(1024)

    if not data:
        break

    log = data.decode()

    print(log)

    parts = log.split("|")

    city = parts[1]

    level = parts[2]

    filename = city.lower() + "_" + level + ".bin"

    binary = log.encode()

    with open(filename, "ab") as file:

        file.write(struct.pack("I", len(binary)))

        file.write(binary)

print("Completed")