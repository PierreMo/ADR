from datetime import datetime
import socket
import time

from server import DEBUG_SERVER, NB_MODULES, connections

def connect_synchronize(s):
    # Accept connections from modules
    while NB_MODULES > len(connections):
        conn, addr = s.accept()
        if DEBUG_SERVER:print(f"Connected by {addr},", end="")
        # Send the current time to the client
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn.sendall(current_time.encode())
        if DEBUG_SERVER:print(f"Time sent: {current_time}")
        connections.append(conn)  # Store the connection
