# Passwordless Blockchain Login - ICAT Project

## Overview

This project allows users to log in **without a password** using a blockchain wallet (MetaMask) and a DID smart contract on the Sepolia testnet.

---

## Prerequisites

1. **MetaMask** installed in your browser
2. MetaMask connected to **Sepolia testnet**
3. **Python 3.10+** installed
4. Internet connection

---

## Setup Instructions

### 1. Clone the project

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install Python dependencies

```bash
pip install flask flask-cors eth-account
```
Right — for a normal user who just wants to run your page locally, the **dependencies are only needed for the backend (Python/Flask)**. The frontend is just HTML/JS and runs in the browser, no install needed.

Here’s how a user would do it step by step:

---

### 1️⃣ Install Python

* Go to [python.org](https://www.python.org/downloads/) and download **Python 3.10+**
* During installation, **check “Add Python to PATH”** (important!)

### 2️⃣ Install backend dependencies

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux), then run:

```bash
pip install flask flask-cors eth-account
```

* `flask` → runs the backend server
* `flask-cors` → allows your frontend (browser) to talk to backend
* `eth-account` → used for verifying Ethereum signatures

---

### 3️⃣ Start the backend server

Navigate to the folder where `app.py` is:

```bash
cd path\to\project-folder
python app.py
```

* The server should start and say something like:
  `* Running on http://127.0.0.1:5000/`

---

### 4️⃣ Open the frontend

* Open `project.html` **in a browser** (Chrome/Edge/Firefox)
* Make sure **MetaMask is installed** and connected to **Sepolia testnet**

Now the user can **connect wallet, register, login, see protected content, logout**.

---


### 3. Run the backend

```bash
python app.py
```

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

## Notes

* The page works **locally**; no internet hosting required
* Animations and notifications are built-in for registration/login

---

