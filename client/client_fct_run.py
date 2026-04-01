from datetime import datetime
import time

from __init__ import CLIENT_DEBUG

def run(s):
    print("Starting radar...")
    # running loop of the radar
    while True:
        vector = (datetime.now().strftime("%M:%S"), datetime.now().strftime("%M:%S"))
        score = 99
        data_packet = f"{"vecteur_heure "},{vector[0]},{vector[1]},{score}"
        s.sendall(data_packet.encode())
        if CLIENT_DEBUG: print(f"Sent: {data_packet}")
        time.sleep(0.04)
