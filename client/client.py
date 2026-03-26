import socket  # to communicate with TCP
import time
from datetime import datetime
import os
from mpu6050 import mpu6050  # gyroscpope
# Initialisation of the MPU-6050 sensor at address I2C 0x68.
sensor = mpu6050(0x68)

HOST = '192.168.137.1'  # Remplace par l'IP de ton PC
PORT = 65432


def set_system_time(new_time_str):
    # Format : "2026-03-24 15:30:00"
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    timestamp = dt.timestamp()
    os.system(f"sudo date -s '{new_time_str}'")

def wait_until_time(new_time_str):
    # adjusting to format
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    # computing time to wait
    current_time = datetime.now()
    time_remaining = dt - current_time

    # Wait until the target time
    if time_remaining.total_seconds() > 0:
        time.sleep(time_remaining.total_seconds())
    else:
        print("The target time is in the past.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Press enter to synchronize")
    input()
    # SYNCHRONISATION
    print("Request time from server...")
    s.connect((HOST, PORT))
    # Receive data from the server
    data = s.recv(1024).decode()
    set_system_time(data)
    print("Raspberry Pi time updated !")

    # CALIBRATING

    # Récupérer les données du gyroscope.
    gyro_data = sensor.get_gyro_data()

    # Afficher les données du gyroscope.
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))


    while not data:
        data = s.recv(1024).decode()
    wait_until_time(data)

    # SENDING DATA FLUX

    # Send data to the server
    while True:
        vector = (datetime.now().strftime("%M:%S"),datetime.now().strftime("%M:%S"))
        score = 99
        data_packet = f"{vector[0]},{vector[1]},{score}"
        s.sendall(data_packet.encode())
        time.sleep(0.04)
