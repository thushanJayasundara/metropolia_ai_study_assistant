# 📘 Metropolia AI Study Assistant  
Live Demo: **https://metropolia-ai-study-assistant.onrender.com/**  

A lightweight 3-tier Flask application that uses OpenAI to help Metropolia students summarize, explain, and understand course materials.  
Built for the AI/Software Engineering assignment with a focus on clean architecture, separation of concerns, and secure deployment practices.

## 🚀 Features

### 🔹 AI-powered Study Help  
Paste any lecture notes or assignment text and choose:

- **Summary (5–10 concise bullet points)**  
- **Beginner-friendly explanation**  
- **Practice questions + answers**  
- **7–14 day study / implementation plan**

### 🔹 3-tier Architecture  
The project is structured into clear layers:

- **Presentation (Frontend)** → HTML, Bootstrap UI  
- **Application / Business Logic (Backend)** → Flask routes + services  
- **Data Layer** → SQLite database storing recent history

### 🔹 Full OpenAI Integration  
All responses are generated using OpenAI (`gpt-4o-mini`).  
Key is securely injected through environment variables (not stored in code).

### 🔹 Deployment on Render  
Deployed as a public web service using Gunicorn + Render’s free tier.

## 🧱 Project Structure

```
metropolia_ai_study_assistant/
│
├─ backend/
│   ├─ app.py               # Flask app factory
│   ├─ config.py            # Environment-based config (OpenAI key, DB path)
│   ├─ ai/                  # AI integration layer
│   ├─ routes/              # Flask Blueprints (presentation endpoints)
│   ├─ services/            # Business logic
│   ├─ models/              # Data models (HistoryEntry)
│   └─ repositories/        # SQLite persistence layer
│
├─ frontend/
│   ├─ templates/           # Jinja2 HTML templates
│   └─ static/              # CSS and frontend assets
│
├─ study_history.db         # SQLite DB (auto-created)
├─ app.py                   # Entry point (used by Gunicorn)
└─ requirements.txt
```

## 🛠️ Local Development

### 1. Clone project  
```bash
git clone https://github.com/your-account/metropolia_ai_study_assistant.git
cd metropolia_ai_study_assistant
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key  
```bash
export OPENAI_API_KEY="your-key-here"
```

### 4. Run the app  
```bash
python3 app.py
```

App runs at: http://127.0.0.1:5000

## 🌐 Deployment (Render)

Build Command:
```
pip install -r requirements.txt
```

Start Command:
```
gunicorn app:app
```

Environment Variables:
```
OPENAI_API_KEY=sk-xxxx
```

Live App:
https://metropolia-ai-study-assistant.onrender.com/

## 📦 Technologies Used

- Python 3.11 / Flask 3  
- OpenAI API (gpt-4o-mini)  
- SQLite  
- Jinja2  
- Bootstrap 5  
- Gunicorn  
- Render
