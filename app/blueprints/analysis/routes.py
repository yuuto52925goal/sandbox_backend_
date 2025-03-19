from flask import request, jsonify, Blueprint
from .service import analyze_feedback
from .analyze_result_dao import AnalyzeResultDAO

analysis_bp = Blueprint('analysis', __name__)

# from models.analyze_result import AnalyzeResult  # Assuming it's in the models folder

# @feedback_analysis_bp.route('/feedback/analyze/<int:company_id>', methods=['GET'])
# def analyze_feedback_by_company(company_id):
#     # Retrieve feedback from the database based on company_id
#     feedback = get_feedback_by_company(company_id)  # Assume this function is defined elsewhere

#     if not feedback:
#         return jsonify({'error': 'No feedback found for the given company ID'}), 404

#     # Pass feedback to the analyze_feedback function in service.py
#     analysis_result = analyze_feedback(feedback)

#     # Store the result in the AnalyzeResult table
#     new_analysis = AnalyzeResult(company_id=company_id, result=analysis_result)
#     db.session.add(new_analysis)
#     db.session.commit()

#     return jsonify({'message': 'Analysis completed successfully', 'result': analysis_result}), 200


@analysis_bp.route('/get_analyze_result', methods=["GET"])
def get_analyze_result():
    body = request.get_json()
    id = str(body.get('company_id'))
    if not id:
        return jsonify({"error: company id is missing"}), 400

    data = AnalyzeResultDAO.get_analyze_result_by_company_id(id)

    return jsonify({"message": data}), 200