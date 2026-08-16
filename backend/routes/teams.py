from flask import Blueprint, jsonify
from services.jolpica import get_wikipedia_image

teams_bp = Blueprint('teams', __name__)

CAR_WIKI_TERMS = {
    '2021': {
        'Red Bull Racing': 'Red Bull Racing RB16B',
        'Mercedes': 'Mercedes F1 W12 E Performance',
        'Ferrari': 'Ferrari SF21',
        'McLaren': 'McLaren MCL35M',
        'Aston Martin': 'Aston Martin AMR21'
    },
    '2022': {
        'Red Bull Racing': 'Red Bull Racing RB18',
        'Ferrari': 'Ferrari F1-75',
        'Mercedes': 'Mercedes F1 W13 E Performance',
        'McLaren': 'McLaren MCL36',
        'Alpine': 'Alpine A522'
    },
    '2023': {
        'Red Bull Racing': 'Red Bull Racing RB19',
        'Mercedes': 'Mercedes F1 W14 E Performance',
        'Ferrari': 'Ferrari SF-23',
        'McLaren': 'McLaren MCL60',
        'Aston Martin': 'Aston Martin AMR23'
    },
    '2024': {
        'McLaren': 'McLaren MCL38',
        'Red Bull Racing': 'Red Bull Racing RB20',
        'Ferrari': 'Ferrari SF-24',
        'Mercedes': 'Mercedes F1 W15 E Performance',
        'Aston Martin': 'Aston Martin AMR24'
    },
    '2025': {
        'McLaren': 'McLaren MCL39',
        'Red Bull Racing': 'Red Bull Racing RB21',
        'Ferrari': 'Ferrari SF-25',
        'Mercedes': 'Mercedes F1 W16 E Performance',
        'Aston Martin': 'Aston Martin AMR25'
    }
}

@teams_bp.route('/car-images/<int:year>', methods=['GET'])
def get_car_images(year):
    terms = CAR_WIKI_TERMS.get(str(year), {})
    result = {}
    for team, search_term in terms.items():
        img = get_wikipedia_image(search_term)
        result[team] = img
    return jsonify(result)