from flask import Flask, request, jsonify
from flask_cors import CORS
from eth_account.messages import encode_defunct
from web3 import Web3
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Temporary storage
challenges = {}         # stores challenges per address
logged_in_users = {}    # stores which users passed login

w3 = Web3()  # Web3 instance

# --- Step 1: Send challenge ---
@app.route('/challenge', methods=['POST'])
def send_challenge():
    data = request.json
    address = data['address']
    
    # Random numeric challenge
    challenge = f"LOGIN_CHALLENGE_{random.randint(100000,999999)}"
    
    # Store challenge
    challenges[address] = challenge
    return jsonify({'challenge': challenge})

# --- Step 2: Verify signature ---
@app.route('/verify', methods=['POST'])
def verify_signature():
    data = request.json
    address = Web3.to_checksum_address(data['address'])
    signature = data['signature']
    challenge = data['challenge']

    stored_challenge = challenges.get(address)
    if stored_challenge != challenge:
        return jsonify({'status': 'error', 'message': 'Challenge mismatch'}), 400

    message = encode_defunct(text=challenge)
    signer_address = w3.eth.account.recover_message(message, signature=signature)

    if signer_address.lower() == address.lower():
        logged_in_users[address] = True  # mark as logged in
        return jsonify({'status': 'success', 'message': 'Authentication successful'})
    else:
        return jsonify({'status': 'error', 'message': 'Signature invalid'}), 400

# --- Step 3: Get protected content ---
@app.route('/get_content', methods=['POST'])
def get_content():
    data = request.get_json()
    address = data.get('address')

    if logged_in_users.get(address):
        content = """
        <h2>Protected Content</h2>
        <p>This content is secure and only sent from the backend after login.</p>
        <ul>
            <li>Secret project details</li>
            <li>Important company files </li>
            etc
        </ul>
        """
        return jsonify({'status': 'success', 'content': content})
    else:
        return jsonify({'status': 'fail', 'message': 'Unauthorized'})

# --- Run app ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
