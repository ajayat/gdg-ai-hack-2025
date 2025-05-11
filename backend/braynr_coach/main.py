from pathlib import Path
from dotenv import load_dotenv
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline

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

questions = pd.read_csv(DATA_DIR / "Chapter1_Q.csv", sep=";")
# Loads a classifier finetuned for Natural Language Inference task
classifier = pipeline("text-classification", "ajayat/xlm-roberta-large-xnli")
history = []  # Store feedback history


@app.get("/", response_class=HTMLResponse)
async def root():
    with open(STATIC_DIR / "html/default.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)


@app.get("/question")
def get_question():
    return {"question": questions.sample(1)["Q"].values[0]}


class QuizItem(BaseModel):
    question: str
    answer: str


@app.post("/score")
async def evaluate_quiz(item: QuizItem):
    # Match the correct answer
    match = questions[questions["Q"] == item.question]
    if match.empty:
        return {"score": 0, "answer": "No answer available"}

    correct_answer = match.iloc[0]["A"]
    # Provide input as a dictionary with text and text_pair keys
    result = classifier({"text": item.answer, "text_pair": correct_answer}, top_k=None)
    # Extract the score from the result
    df = pd.DataFrame(result)
    score = df[df["label"] == "LABEL_0"]["score"].values[0]
    return {"score": round(score * 100), "answer": correct_answer}


class FeedbackInput(BaseModel):
    question: str
    feedback: int  # 1 = like, 0 = dislike


@app.post("/feedback")
def receive_feedback(data: FeedbackInput):
    history.append({"question": data.question, "feedback": data.feedback})
    # TODO: some logic to train the model with the feedback
    print(f"Feedback received: {data.question} - {data.feedback}")
