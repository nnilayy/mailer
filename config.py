# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')  # Use App Password if using Gmail
VERCEL_APP_URL = os.getenv('VERCEL_APP_URL')
