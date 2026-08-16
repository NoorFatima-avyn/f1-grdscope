from flask import Blueprint, jsonify
from services.jolpica import get_race_winner, get_season_races

races_bp = Blueprint('races', __name__)

@races_bp.route('/<int:year>/<int:round_num>/winner', methods=['GET'])
def get_winner(year, round_num):
    data = get_race_winner(year, round_num)
    return jsonify(data)

@races_bp.route('/<int:year>', methods=['GET'])
def get_races(year):
    data = get_season_races(year)
    return jsonify(data)