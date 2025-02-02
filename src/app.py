# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if verify_token == 'your_verify_token_here':
            return challenge
        return 'Verification token mismatch', 403
    elif request.method == 'POST':
        # Itt kezelheted a bejövő üzeneteket
        return 'Event received', 200

if __name__ == '__main__':
    app.run(debug=True)
