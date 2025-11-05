from flask import jsonify


def validate_request(data):
    if not data or "text" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field 'text'."
        }), 400

    if "style" not in data or not data["style"]:
        data["style"] = "concise"
    return None


def success_response(summary_result):
    return jsonify(summary_result), 200
