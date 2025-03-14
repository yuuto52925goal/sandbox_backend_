from . import fetch_feedback_blueprint
from flask import jsonify, request
from ..services.googlemap_service import GooglemapService

@fetch_feedback_blueprint.route("/get_feedback", methods=["GET"])
def fetch_feedback():
    return "Hello"


@fetch_feedback_blueprint.route("/get_feedback", methods=["POST"])
def get_feedback():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
         
        place_id = str(data.get('place_id'))
        if not place_id:
            return jsonify({"error": "place_id is required"}), 400 
        feedback_result = GooglemapService().get_feedback(place_id)
        print("hello")
        return jsonify({"message": feedback_result}), 200
    except Exception as e:
        assert e
        return jsonify({"error": f"invalid call {e}"}), 500