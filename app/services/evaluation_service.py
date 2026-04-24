from app.core.scoring import compute_score

def evaluate_response(prompt: str, response: str):
    score = compute_score(response, prompt)

    return {
        "score": score,
        "normalized": score / 3,
        "status": "PASS" if score >= 2 else "FAIL"
    }