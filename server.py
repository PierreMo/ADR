# server.py (à exécuter sur chaque Raspberry Pi)
import socket

HOST = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
PORT = 65432      # Port arbitraire

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur démarré sur {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connecté par {addr}")
            data = conn.recv(1024)
            if not data:
                break
            print(f"Reçu : {data.decode()}")
            conn.sendall(b"Message recu !")
