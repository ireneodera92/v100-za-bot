import os, threading, time, websocket, json
from flask import Flask
app = Flask(__name__)
TOKEN = os.getenv("DERIV_TOKEN")
def run():
 while True:
  try:
   print("Connecting Deriv...")
   ws = websocket.create_connection("wss://ws.derivws.com/websockets/v3?app_id=1089")
   ws.send(json.dumps({"authorize": TOKEN}))
   print(ws.recv())
   print("DERIV CONNECTED - V100")
   while True:
    time.sleep(30)
  except Exception as e:
   print(e)
   time.sleep(10)
@app.route('/')
def home():
 return "V100 DERIV BOT LIVE"
threading.Thread(target=run, daemon=True).start()
