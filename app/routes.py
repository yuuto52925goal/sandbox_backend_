from flask import Blueprint, jsonify
from flask import Blueprint, current_app, jsonify

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def home():
    try:
        supabase = current_app.config.get('SUPABASE')

        response = supabase.table('company').select('*').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)})