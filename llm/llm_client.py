from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(messages, temperature=0):

    prompt = ""
    for msg in messages:
        prompt += f"{msg['role'].upper()}:\n{msg['content']}\n\n"

    response = client.models.generate_content(
        model="models/aqa",
        contents=prompt,
        config={
            "temperature": temperature,
        }
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return text
