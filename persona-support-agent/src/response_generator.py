import os
from dotenv import load_dotenv
from google import genai

from src.persona_detector import detect_persona
from src.rag_pipeline import search_documents

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_response(user_message):

    persona = detect_persona(user_message)

    results = search_documents(user_message)

    context = "\n".join(results["documents"][0])

    prompt = f"""
    Persona: {persona}

    Knowledge Base:
    {context}

    User Query:
    {user_message}

    Answer using ONLY the knowledge base information.

    Persona Style:
    - Technical Expert: detailed technical explanation
    - Frustrated User: empathetic and reassuring
    - Business Executive: concise and impact-focused
    """

    return persona, f"Mock Response for {persona}\n\n{context}"