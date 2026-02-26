from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your actual Bot Token and Chat ID
TOKEN = "8331823363:AAHdP-pUBCwjEp8JRdjDv033BwrkyxUpEZg"
CHAT_ID = "6543900267"

@app.route('/inject', methods=['POST'])
def inject():
    data = request.json
    number = data.get('number')
    payload = data.get('payload')
    
    # This sends the message to your Telegram
    text = f"🚀 New Injection!\nTarget: {number}\nType: {payload}"
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}")
    
    return {"status": "sent"}, 200

if __name__ == "__main__":
    app.run()
