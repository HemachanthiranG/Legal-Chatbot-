import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",  # Update the model if needed
    "messages": [{"role": "user", "content": "What is contract law?"}]
}

response = requests.post(GROQ_ENDPOINT, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
