# app/routes.py
from flask import Blueprint, request, jsonify, current_app
import requests

main = Blueprint('main', __name__)

def query_gradientai(prompt):
    url = current_app.config['GRADIENT_AI_URL']
    max_tokens = current_app.config['MAX_TOKENS']
    temperature = current_app.config['TEMPERATURE']
    
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'temperature': temperature,
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

@main.route('/ask', methods=['POST'])
def ask():
    data = request.json
    if 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400

    prompt = data['prompt']
    try:
        result = query_gradientai(prompt)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500