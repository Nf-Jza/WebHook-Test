from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])  # ← POST must be here!
def webhook():
    data = request.json
    print("Webhook received:", data)
    return "OK", 200