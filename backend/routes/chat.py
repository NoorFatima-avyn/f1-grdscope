from flask import Blueprint, jsonify, request
from services.ai_chat import get_f1_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')
    year = data.get('year', 2024)
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = get_f1_response(user_message, year)
    return jsonify({'response': response})