
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object('config.Config')

    # Enable CORS
    CORS(app)

    # Register Blueprints
    from app.routes.api import api_bp
    from app.routes.main import main_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(main_bp)

    return app
