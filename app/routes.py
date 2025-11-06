from flask import Flask, Blueprint, request, jsonify
from .summarizer import summarize_text

api = Blueprint("api", __name__)
app = Flask(__name__)

@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Text Summarizer API is running!",
        "available_endpoints": ["/a2a/summarize"],
        "creator": "Your Name"
    }), 200


@api.route("/a2a/summarize", methods=["POST"])
def summarize_a2a():
    """
    Handles both Telex A2A JSON-RPC and normal REST requests.
    """
    try:
        data = request.get_json(force=True)

        if "jsonrpc" in data and "params" in data:
            message_parts = data["params"].get("message", {}).get("parts", [])
            user_text = ""

            for part in message_parts:
                if part.get("kind") == "text":
                    user_text = part.get("text", "")
                    break

            if not user_text:
                return jsonify({
                    "jsonrpc": "2.0",
                    "id": data.get("id", ""),
                    "error": {
                        "code": -32602,
                        "message": "Missing 'text' in message parts"
                    }
                }), 400

            result = summarize_text(user_text)

            return jsonify({
                "jsonrpc": "2.0",
                "id": data.get("id", ""),
                "result": {
                    "id": "task-001",
                    "contextId": "context-id",
                    "status": {
                        "state": "completed",
                        "timestamp": "2025-11-06T00:00:00.000Z",
                        "message": {
                            "messageId": "msg-uuid",
                            "role": "agent",
                            "parts": [
                                {
                                    "kind": "text",
                                    "text": result["summary"]
                                }
                            ],
                            "kind": "message",
                            "taskId": "task-001"
                        }
                    },
                    "artifacts": [],
                    "kind": "task"
                }
            }), 200

        elif "text" in data:
            text = data["text"]
            style = data.get("style", "concise")
            result = summarize_text(text, style)
            return jsonify(result), 200

        else:
            return jsonify({
                "status": "error",
                "message": "Invalid request format. Expecting A2A or 'text'."
            }), 400

    except Exception as e:
        return jsonify({
            "jsonrpc": "2.0",
            "error": {
                "code": -32000,
                "message": f"Server error: {str(e)}"
            }
        }), 500
