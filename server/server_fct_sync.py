from datetime import datetime
import socket
import time

def connect_synchronize(nb_modules, connections, s):
    # Accept connections from modules
    while nb_modules > len(connections):
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        # Send the current time to the client
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.sendall(current_time.encode())
        print(f"Time sent: {current_time}")
        connections.append(conn)  # Store the connection
