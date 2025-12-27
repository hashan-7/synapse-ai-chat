### Synapse AI Chat 🧠✨

Your Intelligent Gateway to Real-Time Knowledge & Deep Research.

Synapse AI Chat is a comprehensive AI-powered assistant designed for real-time information retrieval and deep analysis. Unlike static AI models, Synapse leverages a Search-First Approach, fetching the latest data from the web, academic journals, and video platforms to ensure answers are factual and current.


# ✨ Core Features

 * 🔍 Search-First Architecture: Prioritizes live web data using Google Custom Search API to ensure high factual accuracy.

 * 🎓 Deep Research Engine: Conducts academic-level research, aggregates multiple sources, and generates structured PDF reports with citations.

 * 🖼️ Multimodal AI Support:

 * Create Image: Generate high-quality images from text prompts.

 * Describe Image: Analyze and explain uploaded images.

 * Search Image: Find relevant images from across the web.

 * 🎥 Video Intelligence: Fetches and contextualizes relevant YouTube videos using the YouTube Data API v3.

 * 💬 Intelligent Chat: Engages in natural, context-aware conversations powered by the Google Gemini API.

 * 🔐 Secure Authentication: Secure user login and session management handled via Google OAuth 2.0.


# 🛠️ Tech Stack

This project is built with a reliable and modern technology stack:


## Component

Technology Used

 * Backend :  Python, Flask, Flask-SQLAlchemy

* Database : MySQL (Cloud/Local)

* AI Models : Google Gemini API (Pro/Flash)

* Search APIs : Google Custom Search, YouTube Data API v3

* Frontend : HTML5, CSS3, Vanilla JavaScript (No frameworks)

* PDF Engine : jsPDF, html2canvas

* Auth : Google OAuth 2.0



# ⚙️ Getting Started

Follow these steps to set up Synapse AI Chat locally on your machine.

✅ Prerequisites

Python 3.10+

MySQL Server

Google Cloud Console Account (for API Keys)

🔧 Installation & Setup

Clone the Repository:


git clone [https://github.com/hashan-7/synapse-ai-chat.git](https://github.com/hashan-7/synapse-ai-chat.git)
cd synapse-ai-chat


Create Virtual Environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Install Dependencies:

pip install -r requirements.txt


Configure Environment Variables:
Create a .env file in the root directory and add your credentials. (This file is ignored by Git for security).

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Database Configuration
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@localhost/synapse_db

# AI & Search APIs
GOOGLE_API_KEY=your_gemini_api_key
SEARCH_API_KEY=your_google_search_api_key
SEARCH_ENGINE_ID=your_search_engine_id

# OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret


Initialize Database:

flask db init
flask db migrate
flask db upgrade


Run the Application:

flask run


Access the app at: http://localhost:5000

🤝 Contributing

Contributions are welcome! If you'd like to improve the UI or add new features, feel free to open an issue or submit a pull request.

<p align="center">
Made with by <b>hashan-7</b>
</p>
