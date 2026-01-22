# Blockchain Passwordless Login Project

## Requirements
- Python 3.11+
- MetaMask extension installed on Chrome/Edge/Firefox

## Setup
1. Install dependencies
   pip install -r requirements.txt
2. Run backend:
   python app.py
3. Open frontend (index.html) locally or via GitHub Pages
4. Click "Connect Wallet", then "Login"

## Flow
1. Connect MetaMask wallet
2. Backend generates challenge
3. User signs challenge with wallet
4. Backend verifies signature
5. Protected content displayed
