
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-120b"

def generate_summary(text):
    text = text[:6000]
    prompt = f"""
Create a clear and easy-to-understand summary
using only the study material below.

Organize the summary with headings and important points.
Make it useful for exam preparation.

Study Material:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content


def generate_quiz(text):
    text = text[:6000]
    prompt = f"""
Create 5 multiple-choice questions from the study material.

For each question:
- Give 4 options (A, B, C, D).
- Mention the correct answer.
- Add a short explanation for the answer.
- Keep the questions useful for exam preparation.

Use only the given study material.

Study Material:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content


def generate_two_marks(text):
    text = text[:6000]
    prompt = f"""
Create 5 important 2-mark questions from the study material.

For each question:
- Write the question.
- Give a simple, short answer.
- Focus on important definitions and concepts.

Use only the given study material.

Study Material:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content
