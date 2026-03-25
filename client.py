import socket
import time
from datetime import datetime
import os

HOST = '192.168.137.1'  # Remplace par l'IP de ton PC
PORT = 65432


def set_system_time(new_time_str):
    # Format : "2026-03-24 15:30:00"
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    timestamp = dt.timestamp()
    os.system(f"sudo date -s '{new_time_str}'")

def wait_until_time(new_time_str):
    # adjusting to format
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    # computing time to wait
    current_time = datetime.now()
    time_remaining = dt - current_time

    # Wait until the target time
    if time_remaining.total_seconds() > 0:
        time.sleep(time_remaining.total_seconds())
    else:
        print("The target time is in the past.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Receive data from the server
    data = s.recv(1024).decode()
    set_system_time(data)
    print("Raspberry Pi time updated !")

    while not data:
        data = s.recv(1024).decode()
    wait_until_time(data)

    # Send data to the server
    while True:
        vector = (datetime.now().strftime("%M:%S"),datetime.now().strftime("%M:%S"))
        score = 99
        data_packet = f"{vector[0]},{vector[1]},{score}"
        s.sendall(data_packet.encode())
        time.sleep(0.04)
