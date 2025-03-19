from flask import request, jsonify, Blueprint
from .analysis_service import analyze_feedback
from .analyze_result_dao import AnalyzeResultDAO

analysis_bp = Blueprint('analysis', __name__)


@analysis_bp.route('/get_analyze_result', methods=["GET"])
def get_analyze_result():
    body = request.get_json()
    id = str(body.get('company_id'))
    if not id:
        return jsonify({"error: company id is missing"}), 400

    data = AnalyzeResultDAO.get_analyze_result_by_company_id(id)

    return jsonify({"result": data}), 200


# @analysis_bp.route('/')