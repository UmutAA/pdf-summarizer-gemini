from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

apiKey = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key = apiKey)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Explain how AI works in simple terms",
)

print(response.text)