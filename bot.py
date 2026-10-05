import os, json, time, threading, requests, websocket
from flask import Flask, request
app = Flask(__name__)
TOKEN = "8751793648:AAEO_DnqcIbqHVl7pvVHPuziKV0NLJN7-7U"
CHAT_ID = "8245941566"
def send(msg, cid=None):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": cid or CHAT_ID, "text": msg}, timeout=10)
    except:
        pass
@app.route('/')
def home():
    return "V100 Bot LIVE! - Irene"
@app.route('/webhook', methods=['POST'])
def webhook():
    d=request.get_json(force=True, silent=True)
    if d and "message" in d:
        chat=d["message"]["chat"]["id"]
        text=d["message"].get("text","")
        if text=="/start":
            send(f"✅ Hi Irene! V100 LIVE! ID:{chat}", chat)
        elif text=="/status":
            send("📊 Bot RUNNING! Watching R_100 0.2% spike", chat)
        else:
            send(f"You said: {text}", chat)
    return "ok"
def on_tick(ws, msg):
    try:
        import json as js
        data=js.loads(msg)
        if "tick" in data:
            send(f"⚡ V100 Price: {data['tick']['quote']}")
    except:
        pass
def on_open(ws):
    ws.send(json.dumps({"ticks": "R_100"}))
def run_ws():
    while True:
        try:
            ws=websocket.WebSocketApp("wss://ws.binaryws.com/websockets/v3?app_id=1089", on_message=on_tick, on_open=on_open)
            ws.run_forever()
        except:
            time.sleep(5)
threading.Thread(target=run_ws, daemon=True).start()
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
