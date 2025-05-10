from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from braynr_coach import STATIC_DIR

app = FastAPI()

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Prompt(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
async def root():
    with open(STATIC_DIR / "html/default.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)


@app.post("/chat")
async def chat(prompt: Prompt):
    # Dummy AI agent logic
    user_input = prompt.message
    reply = f"AI Agent Response to: '{user_input}'"
    return {"response": reply}
