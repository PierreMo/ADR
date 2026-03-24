# client.py (à exécuter sur les raspberry)
import socket

HOST = '192.168.x.x'  # Adresse IP du PC
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ENVOIE DATA DEPUIS RASPBERRY")
    data = s.recv(1024)
    print(f"Reçu : {data.decode()}")
