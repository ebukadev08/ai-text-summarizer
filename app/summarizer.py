import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_text(text: str, style: str = "concise") -> dict:
    """
    Summarizes text using Google's Gemini model.
    style: 'concise', 'detailed', or 'bullet'
    """

    prompt = f"""
    You are a professional AI summarizer.
    Summarize the following text clearly and accurately.
    Keep the tone natural and human-like.
    
    - Input style: {style}
    - Ensure readability and preserve main meaning.
    - Do NOT include unnecessary filler words.
    
    Text:
    {text}
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(prompt)

        return {
            "status": "success",
            "style": style,
            "summary": response.text.strip()
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
