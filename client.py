import requests
import time
import random

url = "http://192.168.1.18:5000/receive"

while True:
    data = {"capteur": random.randint(0, 100)}
    requests.post(url, json=data)
    time.sleep(10)  # Envoie toutes les secondes