from flask import Flask, Blueprint, request, jsonify
from .summarizer import summarize_text
from .utils import validate_request, success_response

api = Blueprint("api", __name__)
app = Flask(__name__)


@api.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Text Summarizer API is running!",
        "available_endpoints": ["/summarize"],
        "creator": "Your Name"
    })


@api.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    validation = validate_request(data)
    if validation:
        return validation

    text = data["text"]
    style = data.get("style", "concise")

    result = summarize_text(text, style)
    return success_response(result)

@app.route("/telex", methods=["POST"])
def telex_agent():
    try:
        data = request.get_json()
        user_message = data.get("data", {}).get("message", "")
        if not user_message:
            return jsonify({
                "status": "error",
                "message": "No input text provided."
            }), 400

        # Call your summarizer
        result = summarize_text(user_message, style="concise")

        return jsonify({
            "status": "success",
            "response": result["summary"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
