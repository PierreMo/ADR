import socket
import time
from datetime import datetime

HOST = '0.0.0.0'  # Écoute sur toutes les interfaces
PORT = 65432

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur démarré sur {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connecté par {addr}")
            # Envoie l'heure actuelle au client
            current_time = get_current_time()
            conn.sendall(current_time.encode())
            print(f"Temps envoyé : {current_time}")