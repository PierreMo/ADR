

def radar_run(connections, s):
    # Infinite loop to listen to messages from modules
    while True:
        for conn in connections:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")