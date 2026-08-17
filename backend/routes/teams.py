from flask import Blueprint, jsonify
from services.jolpica import get_wikipedia_image

teams_bp = Blueprint('teams', __name__)

CAR_WIKI_TERMS = {
    '2021': {
        'Red Bull Racing': 'Red_Bull_Racing_RB16B',
        'Mercedes': 'Mercedes-AMG_F1_W12_E_Performance',
        'Ferrari': 'Ferrari_SF21',
        'McLaren': 'McLaren_MCL35M',
        'Aston Martin': 'Aston_Martin_AMR21'
    },
    '2022': {
        'Red Bull Racing': 'Red_Bull_Racing_RB18',
        'Ferrari': 'Ferrari_F1-75',
        'Mercedes': 'Mercedes-AMG_F1_W13_E_Performance',
        'McLaren': 'McLaren_MCL36',
        'Alpine': 'Alpine_A522'
    },
    '2023': {
        'Red Bull Racing': 'Red_Bull_Racing_RB19',
        'Mercedes': 'Mercedes-AMG_F1_W14_E_Performance',
        'Ferrari': 'Ferrari_SF-23',
        'McLaren': 'McLaren_MCL60',
        'Aston Martin': 'Aston_Martin_AMR23'
    },
    '2024': {
        'McLaren': 'McLaren_MCL38',
        'Red Bull Racing': 'Red_Bull_Racing_RB20',
        'Ferrari': 'Ferrari_SF-24',
        'Mercedes': 'Mercedes_-AMG_F1_W15_E_Performance',
        'Aston Martin': 'Aston_Martin_AMR24'
    },
    '2025': {
        'McLaren': 'McLaren_MCL39',
        'Red Bull Racing': 'Red_Bull_Racing_RB21',
        'Ferrari': 'Ferrari_SF-25',
        'Mercedes': 'Mercedes-AMG_F1_W16_E_Performance',
        'Aston Martin': 'Aston_Martin_AMR25'
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