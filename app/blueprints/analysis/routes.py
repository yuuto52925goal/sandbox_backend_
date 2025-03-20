from flask import request, jsonify, Blueprint
from .analysis_service import AnalysisService
from .analyze_result_dao import AnalyzeResultDAO

analysis_bp = Blueprint('analysis', __name__)


@analysis_bp.route('/get_analyze_result', methods=["POST"])
def get_analyze_result():
    body = request.get_json()
    id = str(body.get('company_id'))
    if not id:
        return jsonify({"error: company id is missing"}), 400

    data = AnalyzeResultDAO.get_analyze_result_by_company_id(id)

    return jsonify({"result": data}), 200


@analysis_bp.route('/categorize', methods=["POST"])
def categorize():
    body = request.get_json()
    company_id = str(body.get('company_id'))
    
    if not company_id:
        return jsonify({"error": "company_id is missing"}), 400

    analysis_service = AnalysisService()
    analysis_service.categorize_feedbacks(company_id)

    return jsonify({"message": "Categorizer completed successfully."}), 200


@analysis_bp.route('/summarize', methods=["POST"])
def summarize():
    body = request.get_json()
    company_id = str(body.get('company_id'))
    
    if not company_id:
        return jsonify({"error": "company_id is missing"}), 400

    analysis_service = AnalysisService()
    analysis_service.summarize_feedbacks(company_id)

    return jsonify({"message": "Summarization completed successfully."}), 200
