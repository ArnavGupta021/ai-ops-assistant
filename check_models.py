import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize client
client = genai.Client(api_key=API_KEY)

# List available models
try:
    models = client.models.list()
    print("Available Models:\n")

    for model in models:
        print(model.name)

except Exception as e:
    print("Error fetching models:", e)
