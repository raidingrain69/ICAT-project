# Passwordless Blockchain Login - ICAT Project

## Overview

This project allows users to log in **without a password** using a blockchain wallet (MetaMask) and a DID smart contract on the Sepolia testnet.

---

## Prerequisites

1. **MetaMask** installed in your browser
2. MetaMask connected to **Sepolia testnet**
3. **Python 3.10+** installed
4. Internet connection
5. If cloning install git from https://git-scm.com/download/win Keep the default options (especially “Add Git to PATH” — very important).


---

## Setup Instructions

### 1️⃣ Clone the repository
Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux) and run:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```


### 2. Install Python dependencies

```bash
pip install flask flask-cors eth-account
```
Right — for a normal user who just wants to run your page locally, the **dependencies are only needed for the backend (Python/Flask)**. The frontend is just HTML/JS and runs in the browser, no install needed.

Here’s how to do it step by step:

---

###  Install Python

* Go to [python.org](https://www.python.org/downloads/) and download **Python 3.10+**
* During installation, **check “Add Python to PATH”** (important!)

### Install backend dependencies

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux), then run:

```bash
pip install flask flask-cors eth-account
```

* `flask` → runs the backend server
* `flask-cors` → allows your frontend (browser) to talk to backend
* `eth-account` → used for verifying Ethereum signatures

---

### 3. Run the backend

```bash
python app.py
```

*Open the folder where app.py is , right click and chose open in terminal and write python app.py to start the server
 
* The backend will run at `http://127.0.0.1:5000`
* Leave this running while using the page

### 4. Open the frontend

* Open `project.html` in a browser
* Make sure MetaMask is connected to Sepolia

### 5. Using the page

1. Click **Connect Wallet**
2. If your wallet is not registered, click **Register Wallet**
3. Click **Login (Sign Message)** to access protected content
4. Use **Logout** to disconnect

---


## I added a alternative view in seprate folder. To view that open the deployment and add view-a/ at the end of the url
