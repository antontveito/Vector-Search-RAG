import os
from dotenv import load_dotenv
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
API_KEY =  os.getenv('OPEN_AI_API_KEY')
