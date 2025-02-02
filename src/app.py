# src/app.py
from flask import Flask, request, jsonify
from security import get_secret

app = Flask(__name__)

# Betöltjük a VERIFY_TOKEN-t a Secret Managerből
verify_token = get_secret('VERIFY_TOKEN')

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == verify_token:
            return request.args.get('hub.challenge')
        return 'Verification token mismatch', 403
    elif request.method == 'POST':
        # Itt kezelheted a bejövő üzeneteket
        return 'Event received', 200

if __name__ == '__main__':
    app.run(debug=True)
