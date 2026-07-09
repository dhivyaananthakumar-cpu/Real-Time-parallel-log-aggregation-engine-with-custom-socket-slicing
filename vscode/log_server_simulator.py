import socket
import random
import time
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

cities = ["Mumbai", "Chennai", "Bangalore"]

levels = ["WARNING", "ERROR", "INFO", "DEBUG"]

messages = {

    "WARNING": [
        "CPU Usage High",
        "Memory Usage High",
        "Disk Almost Full"
    ],

    "ERROR": [
        "Database Failed",
        "Socket Error",
        "Authentication Failed"
    ],

    "INFO": [
        "Server Started",
        "User Login",
        "Backup Completed"
    ],

    "DEBUG": [
        "Variable Initialized",
        "Cache Loaded",
        "Thread Started"
    ]

}

while True:

    city = random.choice(cities)

    level = random.choice(levels)

    message = random.choice(messages[level])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{timestamp}|{city}|{level}|{message}"

    client.send(log.encode())

    print(log)

    time.sleep(2)