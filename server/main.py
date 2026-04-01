import socket
import time

import server_fct_sync as sync
import server_fct_calib as calib
import server_fct_run as run

from __init__ import DEBUG_SERVER, HOST, PORT


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    if DEBUG_SERVER:print(f"Server started on {HOST}:{PORT}")

    # --- Connection and synchronization ---
    sync.connect_synchronize(s)

    time.sleep(2)  # Delay of 2 seconds

    # ------------ Calibration --------------
    calib.calibrate_modules()


    # ----------- Radar Running -------------
    run.radar_run()
