# ⚖️ Legal Chatbot (FastAPI + React)

This is a **Legal Chatbot** powered by **FastAPI (Python) and React (JavaScript)**.  
It uses **LLM (Large Language Models) via the Groq API** to provide AI-powered legal answers.

---

## 📌 Features
✅ User-Friendly Chatbot UI (**React + Tailwind/Bootstrap**)  
✅ **FastAPI Backend** for handling legal queries  
✅ **Groq API integration** for AI-powered legal responses  
✅ **CORS Handling** for frontend-backend communication  
✅ **Docker Support** (Optional)  

---

## 🏗️ Project Structure
legal-chatbot/
│── backend/               # FastAPI backend  
│   ├── main.py            # FastAPI app (LLM Integration)  
│   ├── .env               # API keys (Groq API)  
│   ├── requirements.txt   # Backend dependencies  
│   └── ...  
│  
│── frontend/              # React frontend  
│   ├── src/  
│   │   ├── App.js         # Main React component  
│   │   ├── TestAPI.js     # API call handler  
│   │   ├── config.js      # API Base URL  
│   │   └── styles.css     # Custom styles  
│   ├── package.json       # Frontend dependencies  
│   ├── index.js           # Entry point  
│   ├── public/  
│   ├── Dockerfile         # Frontend Docker setup (optional)  
│   └── ...  
│  
│── .gitignore  
│── README.md  
│── docker-compose.yml     # (Optional)  

yaml
Copy
Edit

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/legal-chatbot.git
cd legal-chatbot
🖥️ Backend Setup (FastAPI)
🔹 Install Dependencies
bash
Copy
Edit
cd backend
pip install -r requirements.txt
🔹 Create a .env File
Inside backend/.env file, add:

ini
Copy
Edit
GROQ_API_KEY=your_api_key_here
🔹 Run the FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
✅ FastAPI will be running on:
📌 http://127.0.0.1:8000

🎨 Frontend Setup (React)
🔹 Install Dependencies
bash
Copy
Edit
cd frontend
npm install
🔹 Start the React App
bash
Copy
Edit
npm start
✅ React App will be running on:
📌 http://localhost:3000

⚡ API Endpoints
Method	Endpoint	Description
POST	/ask	Get legal advice from the chatbot
Example Request:
json
Copy
Edit
{
  "question": "What are my rights as a tenant?"
}
Example Response:
json
Copy
Edit
{
  "answer": "As a tenant, you have the right to a safe and habitable living space..."
}
🎯 To-Do List
🔹 Add authentication for user sessions
🔹 Store chat history in a database (SQLite/PostgreSQL)
🔹 Deploy on AWS / Vercel / Render

✨ Contributing
Want to improve this project?
Feel free to fork and create a pull request! 🚀

📄 License
