from dotenv import load_dotenv
import os
from google import genai
import PyPDF2

load_dotenv()

apiKey = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key = apiKey)

pdf_path = input("PDF Path Here: ")
pdf_text = ""

with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        pdf_text += page.extract_text()

prompt = (
    "You are a helpful assistant willing to help me learn things with ease. "
    "Summarize the text below in a few sentences and give me the key words I need to learn:\n\n"
    + pdf_text
)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents = prompt
)

print(response.candidates[0].content)