import socket
import time
import datetime as datt

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432

NB_MODULES = 3
NB_CONN_MODULES = 0
connections = []  # List to store connections


def get_current_time(delay = 0):
    return (datt.datetime.now() + datt.timedelta(0, 20)).strftime("%Y-%m-%d %H:%M:%S")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")

    # Accept connections from modules
    while NB_MODULES > NB_CONN_MODULES:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        # Send the current time to the client
        current_time = get_current_time()
        conn.sendall(current_time.encode())
        print(f"Time sent: {current_time}")
        connections.append(conn)  # Store the connection
        NB_CONN_MODULES += 1

    # Wait for a short delay before sending the green light
    time.sleep(2)  # Delay of 2 seconds (adjustable)
    print("Sending green light to all modules...")
    green_light = get_current_time()  # they can start sending data in 20s
    for conn in connections:
        conn.sendall(green_light.encode())

    # Infinite loop to listen to messages from modules
    while True:
        for conn in connections:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
