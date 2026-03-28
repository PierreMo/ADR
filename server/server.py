import socket
import time

import server_fct_sync as sync
import server_fct_calib as calib
import server_fct_run as run

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432

NB_MODULES = 1
connections = []  # List to store connections

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")

    # --- Connection and synchronization ---
    sync.connect_synchronize(NB_MODULES, connections, s)

    time.sleep(2)  # Delay of 2 seconds

    # ------------ Calibration --------------
    calib.calibrate_modules(connections, s)


    # ----------- Radar Running -------------
    run.radar_run(connections, s)
