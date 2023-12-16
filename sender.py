import time
import socket

from random import randint

HOST = "127.0.0.1"
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        with open("data.txt","r") as f:
            data = f.read()
        name, min, max= data.split(",")
        print(name, min, max)
        random_number1 = randint(int(min), int(max))
        s.sendall(f"{random_number1},{name}".encode())
        print(f"Sending: {random_number1},{name}")
        time.sleep(5)
