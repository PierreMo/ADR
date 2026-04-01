from __init__ import DEBUG_SERVER, connections


def radar_run():
    # Infinite loop to listen to messages from modules
    while True:
        for conn in connections:
            data = conn.recv(1024)
            if not data:
                break
            if DEBUG_SERVER:print(f"Received: {data.decode()}")
