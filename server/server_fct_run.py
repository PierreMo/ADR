from datetime import datetime as datetime, timedelta as timedelta

from __init__ import DEBUG_SERVER, connections


def radar_run():
    if DEBUG_SERVER:print("Sending start time to all modules...")
    # calibration in 10 sec
    calibration_time = (datetime.now() + timedelta(0, 2)).strftime("%Y-%m-%d %H:%M:%S")
    for conn in connections:
        conn.sendall(calibration_time.encode())

    print("Listening radars...")
    if DEBUG_SERVER:print("connections: ", connections)
    # Infinite loop to listen to messages from modules
    while True:
        for conn in connections:
            data = conn.recv(1024)
            if not data:
                break
            if DEBUG_SERVER:print(f"Received: {data.decode()}")
