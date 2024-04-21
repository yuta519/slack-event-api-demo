import requests
from flask import Flask, request, jsonify


app = Flask(__name__)

def verify_request_signature(request):
    signature = request.headers.get("X-Slack-Signature")
    timestamp = request.headers.get("X-Slack-Request-Timestamp")
    # Implement signature verification logic here
    return True  # Return True if signature is valid, False otherwise

def handle_message_event(event_data):
    message = event_data.get("event")
    if message and message.get("type") == "message" and "subtype" not in message:
        channel_id = message.get("channel")
        user_id = message.get("user")
        text = message.get("text")
        # Handle the message event here

@app.route("/slack/events", methods=["POST"])
def post_slack_events():
    if verify_request_signature(request):
        event_data = request.json
        handle_message_event(event_data)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/slack/events", methods=["GET"])
def get_slack_events():
    print(request)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(port=3000)
