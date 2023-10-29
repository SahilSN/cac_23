import os
from dotenv import load_dotenv
from datetime import timedelta
import ssl

APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

class Config:
    OPENAI_API_KEY = os.environ.get('GPT_KEY')