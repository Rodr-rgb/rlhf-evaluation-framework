from fastapi import APIRouter
from app.services.evaluation_service import evaluate_response

router = APIRouter()

@router.post("/evaluate")
def evaluate(payload: dict):
    return evaluate_response(payload["prompt"], payload["response"])