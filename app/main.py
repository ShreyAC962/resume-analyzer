from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from app.utils import extract_text_from_pdf, clean_text
from app.model import get_similarity

import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_ollama_response(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model" : "mistral",
        "prompt" : prompt,
        "stream" : False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

@app.get("/", response_class= HTMLResponse)
async def home(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})

@app.get("/analyze")
async def analyze_resume(request : Request,file : UploadFile = File(...),job_description: str = Form(...)
):
    text = extract_text_from_pdf(file.file)
    text = clean_text(text)
    score = get_similarity(text, job_description)

    prompt = f"""
        You are an expert resume reviewer.
        Resume:
        {text}

        Job Description:
        {job_description}

        Give :
        1. Match analysis
        2. Missing skills
        3. Suggestions to improve
    """
    suggestion = get_ollama_response(prompt)
    return templates.TemplateResponse("index.html",{
        "request" : request,
        "score" : score,
        "suggestion" : suggestion
    })