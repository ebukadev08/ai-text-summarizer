from flask import jsonify

def validate_request(data):
    """
    Validates normal API requests (not A2A requests).
    Ensures that 'text' field is present.
    """
    if not data or "text" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field 'text'."
        }), 400
    return None


def success_response(summary_result):
    """
    Formats a standard success JSON response.
    """
    return jsonify(summary_result), 200
