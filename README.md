<div align="center">

Synapse AI Chat 🧠✨

Your Intelligent Gateway to Real-Time Knowledge & Deep Research.

</div>

🌟 Introduction

Synapse AI Chat is a comprehensive AI Research Assistant designed to provide up-to-the-minute information and deep analysis. Unlike traditional LLMs, Synapse utilizes a Search-First Approach, fetching live data from the web, academic journals, and video platforms to ensure every answer is factual, current, and cited.

Built with a robust Python Flask backend and a responsive Liquid Glass UI (Vanilla JS), it bridges the gap between raw web data and intelligent insights.

🚀 Key Features

🔍 Search-First Architecture Leverages Google Custom Search to provide answers based on real-time web intelligence.

🎓 Deep Research Engine Aggregates multiple academic sources to generate structured, in-depth research reports.

🖼️ Multimodal AI Capabilities

Create Image: Generate high-quality visuals from text prompts.

Describe Image: Analyze and explain content within uploaded images.

Search Image: Discover relevant images from across the web.

🎥 Video Intelligence Fetches and contextualizes YouTube videos directly into your chat.

💬 Intelligent Contextual Chat Maintains conversation history for natural, flowing interactions powered by Google Gemini.

🔐 Secure Authentication Privacy-focused user sessions managed via Google OAuth 2.0.

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

Google Custom Search API, YouTube Data API v3

Frontend

HTML5, CSS3 (Liquid Glass UI), Vanilla JavaScript

PDF Engine

jsPDF, html2canvas

Visualization

vis.js (Mind Maps)

⚙️ Getting Started

Follow these steps to set up and run Synapse AI Chat on your local machine.

✅ Prerequisites

Python 3.10+

MySQL Server

Google Cloud Console credentials (API Key & OAuth Client ID)

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


Configure Environment Variables Create a .env file in the root directory and add your keys:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Database
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@localhost/synapse_db

# AI & Search APIs
GOOGLE_API_KEY=your_gemini_api_key
SEARCH_API_KEY=your_google_search_key
SEARCH_ENGINE_ID=your_search_engine_id

# OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret


Initialize Database

flask db init
flask db migrate
flask db upgrade


Run the Application

flask run


Access the app at 👉 http://localhost:5000

🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

<div align="center">

Made with ❤️ by hashan-7

</div>
