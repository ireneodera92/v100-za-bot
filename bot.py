import os, threading, time, json, websocket
from flask import Flask
app = Flask(__name__)
TOKEN = os.getenv("DERIV_TOKEN")
def run():
 while True:
  try:
   print("Connecting Deriv...")
   ws = websocket.create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")
   ws.send(json.dumps({"authorize": TOKEN}))
   print(ws.recv())
   print("DERIV CONNECTED - V100 LIVE - IRENE")
   while True:
    time.sleep(30)
    ws.send(json.dumps({"ping": 1}))
  except Exception as e:
   print(f"Error: {e}")
   time.sleep(10)
@app.route('/')
def home():
 return "V100 DERIV BOT LIVE - IRENE"
threading.Thread(target=run, daemon=True).start()
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=10000)
