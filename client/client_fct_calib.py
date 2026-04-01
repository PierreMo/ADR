from wait import wait_until_time
from __init__ import CLIENT_DEBUG


def calib(s, sensor_gyro):
    # wait for the start time
    data = s.recv(1024).decode()
    if CLIENT_DEBUG:print("Received calibration time: ", data)
    wait_until_time(data)

    # HERREEEEE YOU SHOULD INSERT THE CALIBRATION PROCESS FOR ALL SENSORS
    # treating image
    img = 0

    # Afficher les données du gyroscope.
    gyro_data = sensor_gyro.get_gyro_data()
    gyro = gyro_data['x'] + gyro_data['y'] + gyro_data['z']

    # treating compass
    compass = 0

    # treating gps
    gps = 0


    # sending the calibration data to the server
    data_packet = f"{gyro},{img},{compass},{gps}"
    s.sendall(data_packet.encode())
