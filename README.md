<div align="center">

Synapse AI Chat 🧠✨

Your Intelligent Gateway to Real-Time Knowledge & Deep Research.

</div>

🌟 Introduction

Synapse AI Chat is a comprehensive AI Research Assistant. Unlike standard chatbots, Synapse prioritizes a Search-First Approach, fetching real-time data from the web, academic sources, and videos to provide accurate, up-to-date answers.

Built with a Python Flask backend and a Vanilla JavaScript frontend, it features a powerful Deep Research Engine capable of generating structured PDF reports with citations automatically.

🚀 Key Features

🔍 Search-First Architecture → Prioritizes live web data using Google Custom Search API.

🎓 Deep Research Engine → Conducts in-depth research and generates structured PDF reports (using jsPDF).

🖼️ Multimodal Capabilities →

Create Image: Generate images from text prompts.

Describe Image: Analyze and describe uploaded images.

Search Image: Find relevant images from the web.

🎥 Video Intelligence → Fetches relevant YouTube videos using YouTube Data API v3.

💬 Intelligent Chat → Remembers context using Google Gemini API.

🔐 Secure Authentication → User management via Google OAuth and MySQL.

🛠️ Tech Stack

Component

Technology Used

Backend

Python, Flask, Flask-SQLAlchemy

Database

MySQL (Cloud/Local)

AI Models

Google Gemini API (Pro/Flash)

Search APIs

Google Custom Search, YouTube Data API v3

Frontend

HTML5, CSS3, Vanilla JavaScript

PDF Engine

jsPDF, html2canvas

Auth

Google OAuth 2.0

⚙️ Getting Started

Follow these steps to run Synapse AI Chat locally.

✅ Prerequisites

Python 3.10+

MySQL Server

Google Cloud Console Account (for API Keys)

🔧 Installation & Setup

Clone the Repository

git clone [https://github.com/hashan-7/synapse-ai-chat.git](https://github.com/hashan-7/synapse-ai-chat.git)
cd synapse-ai-chat


Create Virtual Environment

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Configure Environment Variables
Create a .env file in the root directory and add your keys:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key

# Database
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@localhost/synapse_db

# APIs
GOOGLE_API_KEY=your_gemini_key
SEARCH_API_KEY=your_google_search_key
SEARCH_ENGINE_ID=your_search_engine_id

# OAuth
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret


Initialize Database

flask db init
flask db migrate
flask db upgrade


Run the Application

flask run


Visit http://localhost:5000

🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request if you'd like to improve the UI or add features.

<div align="center">
Made with by <b>h7</b>
</div>