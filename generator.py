import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(
    api_key=token
)


def generate_summary(text):

    prompt = f"""
Create a simple and clear summary from the study material below.

Use only the given study material.

Study Material:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1500
    )

    return response.choices[0].message.content


def generate_quiz(text):

    prompt = f"""
Create 5 multiple choice questions from the study material below.

For each question:
- Give 4 options
- Give the correct answer
- Keep questions suitable for students

Study Material:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2000
    )

    return response.choices[0].message.content


def generate_two_marks(text):

    prompt = f"""
Create 5 important 2-mark questions from the study material below.

For each question:
- Give the question
- Give a short and simple answer

Study Material:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1500
    )

    return response.choices[0].message.content