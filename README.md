# StudyMate AI

StudyMate AI is a simple AI-powered study assistant built with Python and Streamlit. It helps students convert study materials into summaries, quizzes, and 2-mark questions.

<img width="737" height="488" alt="image" src="https://github.com/user-attachments/assets/ec90f0a5-a1c2-4ac2-9ec3-c167e3b4a4df" />

## Features

* Upload PDF files
* Upload PPTX presentations
* Upload DOCX documents
* Upload TXT files
* Upload images and extract text using OCR
* Generate AI-powered summaries
* Generate MCQ quizzes
* Generate important 2-mark questions
* Hugging Face API integration
* Streamlit Cloud deployment support

## Technologies Used

* Python
* Streamlit
* Hugging Face
* PyMuPDF
* python-pptx
* python-docx
* Tesseract OCR
* Pytesseract
* Pillow

## Project Structure

```text
Study_Mate_AI/
│
├── app.py
├── generator.py
├── ocr.py
├── pdf_reader.py
├── ppt_reader.py
├── docx_reader.py
│
├── requirements.txt
├── packages.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

bash
git clone https://github.com/nandhinisri1706/Study-Mate-AI.git
cd Study-Mate-AI


Install the required packages:

bash
python -m pip install -r requirements.txt


For image OCR, install Tesseract OCR on your system.

## Environment Variable

Create a `.env` file:

env
HF_TOKEN=your_huggingface_token


Do not upload the `.env` file to GitHub.

## Run the Application

bash
python -m streamlit run app.py


The application will open in your browser.

## AI Features

### Summary

Generates a simple and clear summary from the uploaded study material.
<img width="646" height="480" alt="image" src="https://github.com/user-attachments/assets/785d2586-55d5-4e19-9684-0c94d3e9d915" />
<img width="739" height="456" alt="image" src="https://github.com/user-attachments/assets/286ccb7e-8c21-4c76-95bc-6b6e600c0d25" />
<img width="655" height="305" alt="image" src="https://github.com/user-attachments/assets/0ff96e30-55dd-4609-b940-2b44c927fe63" />
<img width="740" height="574" alt="image" src="https://github.com/user-attachments/assets/7a97d060-3e2a-4961-985f-1e51972e1934" />
<img width="721" height="429" alt="image" src="https://github.com/user-attachments/assets/fd834169-93f2-4d12-932f-68e6e3b5a90e" />
<img width="723" height="510" alt="image" src="https://github.com/user-attachments/assets/16a39271-aaa0-4966-87ce-fdff2301c0fa" />
<img width="651" height="153" alt="image" src="https://github.com/user-attachments/assets/cf42fb83-abf4-4a89-b43e-e9ccfc2c4e4f" />


### Quiz

Generates multiple-choice questions with four options and the correct answer.
<img width="666" height="477" alt="image" src="https://github.com/user-attachments/assets/fd21a0ac-4328-4815-8b6d-c4e7082e19b3" />
<img width="738" height="293" alt="image" src="https://github.com/user-attachments/assets/66fdae3a-6405-4e74-9cdf-dd540cc8f095" />
<img width="676" height="280" alt="image" src="https://github.com/user-attachments/assets/3cd72021-3315-4c5c-9497-a24f99ec5689" />
<img width="762" height="290" alt="image" src="https://github.com/user-attachments/assets/0fc46f0e-b8dc-4cc2-b028-0b7947aed914" />
<img width="672" height="307" alt="image" src="https://github.com/user-attachments/assets/c6f3d498-7c14-49fc-b8f5-c76c6b79876c" />

### 2-Mark Questions

Generates important 2-mark questions along with short and simple answers.
<img width="681" height="588" alt="image" src="https://github.com/user-attachments/assets/53a9f3ca-4667-4267-80b9-b44b8cf9e85c" />
<img width="659" height="356" alt="image" src="https://github.com/user-attachments/assets/a64a0008-6b89-4a86-9450-d50eb17e2242" />

## Streamlit Cloud Deployment

For OCR support on Streamlit Community Cloud, add a `packages.txt` file in the project root:

text
tesseract-ocr


The Hugging Face API token should be added through Streamlit Cloud Secrets instead of uploading the `.env` file.

## Security

* API keys are stored using environment variables or Streamlit Secrets.
* `.env` is excluded using `.gitignore`.
* API keys should never be committed to GitHub.

## Purpose

StudyMate AI is designed to help students prepare for exams by transforming different types of study materials into summaries, quizzes, and short-answer questions using AI.

## Developed By

**Nandhini Sri**

**StudyMate AI — Upload your study material and prepare smarter.**
