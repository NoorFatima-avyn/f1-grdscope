from flask import Blueprint, jsonify
from services.jolpica import get_season_drivers

seasons_bp = Blueprint('seasons', __name__)

@seasons_bp.route('/<int:year>', methods=['GET'])
def get_season(year):
    data = get_season_drivers(year)
    return jsonify(data)
