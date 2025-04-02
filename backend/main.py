from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

# FastAPI app instance
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define request model
class Query(BaseModel):
    question: str

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "Legal Chatbot API is running!"}

# Ask AI endpoint
@app.post("/ask")
def ask_question(query: Query):
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY is missing")

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "llama3-70b-8192",  # Adjust if using a different model
        "messages": [{"role": "user", "content": query.question}]
    }
    
    try:
        response = requests.post(GROQ_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()  # Raises an error for non-200 responses

        ai_response = response.json()
        return {"answer": ai_response["choices"][0]["message"]["content"]}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"AI model failed: {str(e)}")

# Debug endpoint to list available routes
@app.get("/routes")
def get_routes():
    return {"available_routes": [route.path for route in app.routes]}
