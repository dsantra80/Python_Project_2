import requests
from flask import current_app
import threading

#lock = threading.Lock()

#def query_gradientai(prompt, max_tokens, temperature):
#    with lock:
#        url = current_app.config['GRADIENT_AI_URL']
#        payload = {
#            "prompt": prompt,
#            "max_tokens": max_tokens,
#            "temperature": temperature
#         }
#        response = requests.post(url, json=payload)
#        if response.status_code == 200:
#            return response.json().get('generated_text', '')
#        else:
#            return f"Error: {response.status_code}"

def query_gradientai(prompt, max_tokens, temperature, gradient_ai_url):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'prompt': prompt,
        'max_tokens': max_tokens,
        'temperature': temperature
    }
    response = requests.post(gradient_ai_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get('generated_text', 'No response')
    else:
        return 'Error in model inference'
