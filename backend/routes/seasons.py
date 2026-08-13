from flask import Blueprint, jsonify
from services.jolpica import (
    get_season_drivers,
    get_season_races,
    get_driver_standings,
    get_constructor_standings
)

seasons_bp = Blueprint('seasons', __name__)

@seasons_bp.route('/<int:year>/drivers', methods=['GET'])
def get_drivers(year):
    data = get_season_drivers(year)
    return jsonify(data)

@seasons_bp.route('/<int:year>/races', methods=['GET'])
def get_races(year):
    data = get_season_races(year)
    return jsonify(data)

@seasons_bp.route('/<int:year>/driver-standings', methods=['GET'])
def get_driver_standings_route(year):
    data = get_driver_standings(year)
    return jsonify(data)

@seasons_bp.route('/<int:year>/constructor-standings', methods=['GET'])
def get_constructor_standings_route(year):
    data = get_constructor_standings(year)
    return jsonify(data)