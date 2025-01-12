
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask API!"})
