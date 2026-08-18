from flask import Flask, send_from_directory
from flask_cors import CORS
import os

from routes.seasons import seasons_bp
from routes.drivers import drivers_bp
from routes.races import races_bp
from routes.teams import teams_bp
from routes.chat import chat_bp
from routes.predictions import predictions_bp

frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend')

def create_app():
    app = Flask(__name__, static_folder=frontend_path, static_url_path='')
    CORS(app)

    app.register_blueprint(seasons_bp, url_prefix='/api/seasons')
    app.register_blueprint(drivers_bp, url_prefix='/api/drivers')
    app.register_blueprint(races_bp, url_prefix='/api/races')
    app.register_blueprint(teams_bp, url_prefix='/api/teams')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    app.register_blueprint(predictions_bp, url_prefix='/api/predictions')

    @app.route('/')
    def index():
        return send_from_directory(frontend_path, 'index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory(frontend_path, path)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)