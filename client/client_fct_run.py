from datetime import datetime
import time


def run(s):
    # running loop of the radar
    while True:
        vector = (datetime.now().strftime("%M:%S"), datetime.now().strftime("%M:%S"))
        score = 99
        data_packet = f"{vector[0]},{vector[1]},{score}"
        s.sendall(data_packet.encode())
        time.sleep(0.04)
