import socket  # to communicate with TCP
import time
from mpu6050 import mpu6050  # gyroscpope
# Initialisation of the MPU-6050 sensor at address I2C 0x68.
sensor_gyro = mpu6050(0x68)

import client_fct_sync as sync
import client_fct_calib as calib
import client_fct_run as run

from wait import wait_until_time

HOST = '192.168.137.1'  # IP of the PC in the local network (hotspot for now)
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Press enter to synchronize")
    input()

    # --- Connection and synchronization ---
    sync.sync_connect(s, HOST, PORT)

    # ------------ Calibration --------------
    # wait for the start time
    data = s.recv(1024).decode()
    while not data:
        data = s.recv(1024).decode()
    wait_until_time(data)

    gyro, img, compass, gps = calib.calib(s, sensor_gyro)

    #sending the calibration data to the server

    # ----------- Radar Running -------------
    # wait for the start time
    data = s.recv(1024).decode()
    while not data:
        data = s.recv(1024).decode()
    wait_until_time(data)

    run.run(s)
