## AI Text Summarizer — HNG Stage 3 Backend Task

An intelligent AI text summarization agent built with Flask and Google Gemini, designed to summarize long texts into concise, detailed, or bullet-point summaries.
This project is integrated with Telex.im and can be deployed on platforms like Render or Railway.

## Setup Instructions
Clone the Repository
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer

## Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate  # (on Windows)
# OR
source venv/bin/activate  # (on Mac/Linux)

## Install Dependencies
pip install -r requirements.txt

## Create a .env File

Inside your project root, create a .env file and add:

GEMINI_API_KEY=your_gemini_api_key_here

## Run the Application
python run.py


The app will run at:
👉 http://127.0.0.1:5000

## API Usage (via Postman or Telex.im)

Endpoint:
POST /summarize

Request Headers:

Content-Type: application/json


Request Body Example:

{
  "text": "Artificial Intelligence is transforming how humans interact with technology by enabling automation and learning.",
  "style": "bullet"
}


Response Example:

{
  "status": "success",
  "style": "bullet",
  "summary": "• AI automates tasks and enhances human-technology interaction through learning."
}
