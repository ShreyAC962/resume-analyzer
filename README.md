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

# AI Resume Analyzer

This is a FastAPI-based web app that analyzes resumes against a job description using embeddings and a local AI model (Ollama/Mistral).  


## Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd resume-analyzer
````

2. **Create and activate virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*(If you don’t have a `requirements.txt`, install manually:)*

```bash
pip install fastapi uvicorn jinja2 requests python-multipart sentence-transformers
```

---

## Running the App

Run the server from the **project root (`resume-analyzer/`)**:

```bash
uvicorn app.main:app --reload
```

* `--reload` enables hot-reload for development.
* Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

1. Upload your resume PDF.
2. Paste a job description in the textarea.
3. Click **Analyze**.
4. View the match score and AI-generated suggestions.

---

## Notes

* Make sure your **`templates/`** folder is at the project root, not inside `app/`.
* Do **not** clear Jinja2 cache manually (`templates.env.cache.clear()`), it causes `TypeError: unhashable type: 'dict'`.
* Ensure Ollama/Mistral API is running locally at `http://localhost:11434`.

```
