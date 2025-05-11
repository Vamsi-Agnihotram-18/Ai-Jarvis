# 🧠 AI JARVIS – Your Smart Document Assistant

AI JARVIS is an intelligent, full-stack assistant inspired by Iron Man’s J.A.R.V.I.S. It helps users manage documents and extract insights using natural language commands, OCR, and LLMs — all with voice or text input.

## 🚀 Features

- 📄 **Document Understanding** – OCR and NLP to extract content from PDFs and images.
- 🗣️ **Voice Commands** – Transcribe and respond to user queries in natural language.
- 🤖 **GPT-Powered Replies** – Uses OpenAI's GPT to answer based on document content.
- 🔍 **Vector Search** – Fast and relevant retrieval using Pinecone or similar vector DBs.
- ☁️ **Cloud Integration** – Upload/download from Google Drive.
- 📊 **Smart Dashboard** – React-based UI for document summaries and interactions.

## 🛠️ Tech Stack

**Frontend:** React.js, HTML, CSS  
**Backend:** Flask, Python  
**AI/NLP:** OpenAI GPT, EasyOCR, Whisper, BERT  
**Database:** SQLite, Pinecone (Vector DB)  
**Cloud Services:** Google Drive API, Azure OCR (Form Recognizer)  
**Others:** Docker, REST APIs, dotenv

## 📁 Folder Structure

Ai-Jarvis/
├── backend/ # Flask API, OCR, NLP, DB handling
├── frontend/ # React UI for chat, dashboard, upload
├── docker-compose.yml # Optional container setup
├── .gitignore # Ignores secrets, venv, node_modules
└── README.md


## ⚙️ Setup Instructions

### 🔧 Backend

cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
python app.py


### 🌐 Frontend
bash
Copy
Edit
cd frontend
npm install
npm start


🐳 Optional: Docker Compose

docker-compose up --build
🧪 Usage
Upload a document or speak a query.

AI JARVIS processes, retrieves relevant info, and replies.

Browse or download summarized responses.

🔐 Security Notice
All secrets (OpenAI API keys, Google credentials) are stored in .env files and ignored in the repo. Ensure you create your own .env based on the template.

👨‍💻 Contributors
Vamsi
Sruthi
Yashwanth
Varun






