from flask import Flask, Blueprint, request, jsonify
from .summarizer import summarize_text
from .utils import validate_request, success_response

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
    try:
        data = request.get_json(force=True)

        validation = validate_request(data)
        if validation:
            return validation

   
        if data.get("type") == "a2a":
            message = data.get("message", "")
            if not message:
                return jsonify({
                    "type": "a2a-response",
                    "status": "error",
                    "response": "Missing 'message' field in A2A request."
                }), 400

            result = summarize_text(message)
            return jsonify({
                "type": "a2a-response",
                "status": "success",
                "response": result.get("summary", "")
            }), 200

        
        elif "text" in data:
            text = data["text"]
            style = data.get("style", "concise")
            result = summarize_text(text, style)
            return success_response(result)

        
        else:
            return jsonify({
                "status": "error",
                "message": "Invalid format. Use 'text' or A2A 'message'."
            }), 400

    except Exception as e:
        return jsonify({
            "type": "a2a-response",
            "status": "error",
            "response": f"Server error: {str(e)}"
        }), 500
