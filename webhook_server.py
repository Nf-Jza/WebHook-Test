from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received:", data)
    return "OK", 200

# Only include this when testing locally:
# if __name__ == '__main__':
#     app.run(port=5000)
