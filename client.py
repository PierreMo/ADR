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
    # Sous Linux, utilise la commande `date`
    os.system(f"sudo date -s '{new_time_str}'")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024).decode()
    print(f"Temps reçu du serveur : {data}")
    set_system_time(data)
    print("Temps du Raspberry Pi mis à jour !")