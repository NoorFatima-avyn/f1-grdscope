from flask import Flask
from flask_cors import CORS

from routes.seasons import seasons_bp
from routes.drivers import drivers_bp
from routes.races import races_bp
from routes.teams import teams_bp
from routes.chat import chat_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # register all route blueprints
    app.register_blueprint(seasons_bp, url_prefix='/api/seasons')
    app.register_blueprint(drivers_bp, url_prefix='/api/drivers')
    app.register_blueprint(races_bp,   url_prefix='/api/races')
    app.register_blueprint(teams_bp,   url_prefix='/api/teams')
    app.register_blueprint(chat_bp,    url_prefix='/api/chat')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)