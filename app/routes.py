from flask import Blueprint, jsonify
from . import supabase

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    try:
        response = supabase.table('company').select('*', count='exact').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)})