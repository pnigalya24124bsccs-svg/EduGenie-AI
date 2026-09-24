import os
import traceback
from google import genai

# Ungaludde puthiya Google AI Studio API key ingane nalkuka
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

def answer_question(question: str) -> str:
    # Direct-aayi puthiya key maathram edukkum
    active_key = API_KEY.strip()

    if not active_key or "YOUR_NEW" in active_key:
        return "❌ Error: New GEMINI_API_KEY is not set correctly in qna.py"

    try:
        client = genai.Client(api_key=active_key)
        
        # Primary Model Call
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=question
            )
            if response and response.text:
                return response.text
        except Exception:
            # Fallback Model
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=question
            )
            if response and response.text:
                return response.text

        return "❌ Empty response received."

    except Exception as e:
        err_msg = str(e)
        if "429" in err_msg:
            return "⚠️ Rate limit reached for this key. Please wait a minute or use another project key."
        traceback.print_exc()
        return f"❌ Error: {err_msg}"