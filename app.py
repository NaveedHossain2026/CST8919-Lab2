import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging to output to console (which Azure App Service captures)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SecurityLogger")

@app.route('/')
def home():
    return "Demo Security Web App is Running."

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    # Simulate a basic authentication check
    if username == "admin" and password == "SecurePass123":
        logger.info(f"SUCCESSFUL_LOGIN: User '{username}' successfully logged in from IP {request.remote_addr}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logger.warning(f"FAILED_LOGIN: Failed login attempt for user '{username}' from IP {request.remote_addr}")
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)