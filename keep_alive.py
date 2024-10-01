from flask import Flask
from threading import Thread
import requests
import time

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def ping_self():
    while True:
        requests.get("https://USER_NAME.pythonanywhere.com")
        time.sleep(300)  # Espera 5 minutos

if __name__ == "__main__":
    keep_alive()
    ping_thread = Thread(target=ping_self)
    ping_thread.start()