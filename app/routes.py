from flask import Blueprint, request, jsonify, current_app
from app.model import query_gradientai
import threading

main = Blueprint('main', __name__)

def validate_input(data):
    if not isinstance(data, dict):
        return False, "Invalid input format. Expected a JSON object."
    required_keys = ['user_input', 'system_prompt']
    for key in required_keys:
        if key not in data:
            return False, f"Missing required field: {key}"
    return True, None

#@main.route('/generate', methods=['POST'])
#def generate_text():
#    data = request.get_json()
#    is_valid, error_message = validate_input(data)
#    if not is_valid:
#        return jsonify({'error': error_message}), 400

#    user_input = data.get('user_input', '')
#    system_prompt = data.get('system_prompt', '')
#    max_tokens = data.get('max_tokens', current_app.config['MAX_TOKENS'])
#    temperature = data.get('temperature', current_app.config['TEMPERATURE'])

#    prompt = f"{system_prompt}\n{user_input}"
#    result = {}

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('user_input')
    system_prompt = data.get('system_prompt', '')

    if not user_input:
        return jsonify({'error': 'Missing required field: user_input'}), 400

    prompt = system_prompt + " " + user_input if system_prompt else user_input
    result = {}
    gradient_ai_url = app.config['GRADIENT_AI_URL']


#   def model_inference():
#        result['generated_text'] = query_gradientai(prompt, max_tokens, temperature)
#
#    thread = threading.Thread(target=model_inference)
#    thread.start()
#    thread.join()

 #   return jsonify({'generated_text': result.get('generated_text', 'Error in model inference')})

def model_inference(result, prompt, max_tokens, temperature, gradient_ai_url):
    # No need for app.app_context() as we are passing necessary config directly
    result['generated_text'] = query_gradientai(prompt, max_tokens, temperature, gradient_ai_url)
    
    return jsonify(result)    

@main.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'API is running'})
