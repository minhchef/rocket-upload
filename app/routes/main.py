from flask import Blueprint, send_from_directory
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')
    return send_from_directory(static_dir, 'index.html')

@main_bp.route('/assets/<path:filename>')
def serve_assets(filename):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/assets')
    return send_from_directory(static_dir, filename)

@main_bp.route('/tokens/<path:filename>')
def serve_tokens(filename):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/tokens')
    return send_from_directory(static_dir, filename)