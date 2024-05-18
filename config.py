# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GRADIENT_AI_URL = os.getenv('GRADIENT_AI_URL')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 100))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))