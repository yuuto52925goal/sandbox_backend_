from . import fetch_feedback_blueprint

@fetch_feedback_blueprint.route("/get_feedback", methods=["GET"])
def get_feedback():
    return "Hello"