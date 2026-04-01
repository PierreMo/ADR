from datetime import datetime as datetime, timedelta as timedelta

from server import DEBUG_SERVER, connections


def calibrate_modules():
    if DEBUG_SERVER:print("Sending green light to all modules...")
    # calibration in 20 sec
    calibration_time = (datetime.now() + timedelta(0, 20)).strftime("%Y-%m-%d %H:%M:%S")
    for conn in connections:
        conn.sendall(calibration_time.encode())

    # receiving image and data from modules
    calibration_data = []
    for conn in connections:
        calibration_data.append(conn.recv(1024).decode())

    # treating received data
    for data in calibration_data:
        if DEBUG_SERVER:print("Received data from module:", end="")
        print(data)
        # treating gps

        # treating compass

        # treating gyroscope

        # treating image
