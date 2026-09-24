
import os
import traceback
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Custom Modules (Existing files format)
from qna import answer_question
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie AI")

# Mount Static Files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# 1. Ask Q&A (GET)
@app.get("/qa")
async def handle_qa_get(question: str):
    answer = answer_question(question)
    return {"answer": answer}

# 2. Explain Concept
@app.post("/explain")
async def handle_explain(question: str = Form(...)):
    answer = answer_question(question)
    return {"answer": answer}

# 3. Learning Path
@app.post("/learning")
@app.post("/api/learning-path")
async def handle_learning_path(topic: str = Form(...)):
    recommendations = get_learning_recommendations(topic)
    return {"answer": recommendations}

# 4. Generate Quiz
@app.post("/quiz")
@app.post("/api/quiz")
async def handle_quiz(topic: str = Form(...)):
    quiz_data = generate_quiz(topic)
    return {"answer": quiz_data}

# 5. Summarize Paragraph (Directly uses qna.py without needing summarizer.py)
@app.post("/summarize")
async def handle_summarize(text: str = Form(...)):
    summary_prompt = f"Please summarize the following text in a concise and clear manner:\n\n{text}"
    summary = answer_question(summary_prompt)
    return {"answer": summary}