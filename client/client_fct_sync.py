from datetime import datetime
import os


def set_system_time(new_time_str):
    # Format : "2026-03-24 15:30:00"
    dt = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M:%S")
    timestamp = dt.timestamp()
    os.system(f"sudo date -s '{new_time_str}'")


def sync_connect(s, HOST, PORT):
    print("Request time from server...")
    s.connect((HOST, PORT))
    # Receive data from the server
    data = s.recv(1024).decode()
    set_system_time(data)
    print("Raspberry Pi time updated !")