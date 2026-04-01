import socket  # to communicate with TCP
import time
from mpu6050 import mpu6050  # gyroscpope
# Initialisation of the MPU-6050 sensor at address I2C 0x68.
sensor_gyro = mpu6050(0x68)

import client_fct_sync as sync
import client_fct_calib as calib
import client_fct_run as run

from __init__ import HOST, PORT, CLIENT_DEBUG

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Press enter to synchronize")
    input()

    # --- Connection and synchronization ---
    sync.sync_connect(s, HOST, PORT)

    # ------------ Calibration --------------
    calib.calib(s, sensor_gyro)

    # ----------- Radar Running -------------
    run.run(s)
