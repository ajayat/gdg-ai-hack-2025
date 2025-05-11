from pathlib import Path
from tkinter.messagebox import QUESTION
from dotenv import load_dotenv
import random
import pandas as pd

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Define global constants
ROOT_DIR = Path(__file__).parent.parent
STATIC_DIR = ROOT_DIR / "static"
DATA_DIR = ROOT_DIR / "data"

app = FastAPI()

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/", response_class=HTMLResponse)
async def root():
    with open(STATIC_DIR / "html/default.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)


class QuizItem(BaseModel):
    question: str
    answer: str


@app.post("/coach")
async def evaluate_quiz(item: QuizItem):
    # Dummy scoring logic — replace with actual NLP model or rubric logic
    if item.answer.strip():
        score = min(len(item.answer), 100)
    else:
        score = 0
    return {"score": score}


# Mock question list
questions = pd.read_csv(DATA_DIR / "Chapter1_Q.csv", sep=";")
print(questions.head())


@app.get("/question")
def get_question():
    return {"question": questions.sample(1)["Q"].values[0]}


class AnswerInput(BaseModel):
    question: str
    answer: str


@app.post("/score")
def score_answer(item: AnswerInput):
    # Placeholder scoring logic
    score = min(len(item.answer.strip()), 100)
    return {"score": score}
