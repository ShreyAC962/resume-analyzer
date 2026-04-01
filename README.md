## AI Resume Analyzer (LLM + ML Hybrid)
    Uses NLP + embeddings + LLMs (modern stack)
    Shows end-to-end ML pipeline
    Has real-world business value
    Easy to explain in interviews
    Can be deployed live

## Build
A web app where:
    User uploads resume (PDF)
    Inputs job description
    System:
    Extracts text
    Computes similarity
    Gives match score
    Suggests improvements using LLM

## Tech Stack
    Backend: FastAPI
    ML/NLP: Scikit-learn + Sentence Transformers
    LLM: OpenAI (or open-source)
    Frontend: Simple HTML
    Deployment: Render

## Project Structure
```
    resume-analyzer/
    │
    ├── app/
    │   ├── main.py
    │   ├── model.py
    │   ├── utils.py
    │   ├── schemas.py
    │
    ├── templates/
    │   └── index.html
    │
    ├── static/
    │   └── style.css
    │
    ├── requirements.txt
    ├── README.md
```
