from flask import Flask, request, jsonify, render_template
import requests
import subprocess
import time

app = Flask(__name__)

# Rasa server URL
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Adjust the port if necessary

def start_rasa_server():
    """Start the Rasa server as a subprocess."""
    subprocess.Popen(["rasa", "run", "--enable-api", "--cors", "*"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Wait a few seconds for the server to start

def start_rasa_actions():
    """Start the Rasa actions server as a subprocess."""
    subprocess.Popen(["rasa", "run", "actions"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Wait a few seconds for the actions server to start

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the message from the request
    user_message = request.json.get('message')
    
    # Send the message to Rasa
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
    
    # Get the response from Rasa
    if response.status_code == 200:
        rasa_response = response.json()
        return jsonify(rasa_response)
    else:
        return jsonify({"error": "Failed to get response from Rasa"}), 500

if __name__ == '__main__':
    # Start the Rasa server and actions server
    start_rasa_server()
    start_rasa_actions()
    app.run(port=5000)  # You can change the port if needed