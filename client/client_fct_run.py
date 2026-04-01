from datetime import datetime
import time

from __init__ import CLIENT_DEBUG, PACKET_PER_SECOND

def run(s):
    print("Starting radar...")
    microsec_btwn_packets = 1000000 / PACKET_PER_SECOND
    # running loop of the radar
    while True:
        #record time for packet per seconds
        begin_time = datetime.now()

        # creating data packet
        vector = (datetime.now().strftime("%M:%S"), datetime.now().strftime("%M:%S"))
        score = 99
        data_packet = f"{"vecteur_heure "},{vector[0]},{vector[1]},{score}"

        # sending data packet
        s.sendall(data_packet.encode())
        if CLIENT_DEBUG: print(f"Sent: {data_packet}")

        # ensuring packets per seconds
        time_delta = datetime.now().microsecond - begin_time.microsecond
        if time_delta < microsec_btwn_packets:
            time.sleep((microsec_btwn_packets - time_delta) / 1000000.0)