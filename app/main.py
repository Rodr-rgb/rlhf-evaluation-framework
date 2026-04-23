from fastapi import FastAPI
from app.evaluator import evaluate

app = FastAPI()

@app.post("/evaluate")
def run(payload: dict):
    return evaluate(payload["prompt"], payload["response"])