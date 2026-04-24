from app.core.scoring import compute_score

class Evaluator:
    """
    Core evaluator that orchestrates scoring logic.
    This acts as the main engine for RLHF-style evaluation.
    """

    def __init__(self):
        self.version = "1.0"

    def evaluate(self, prompt: str, response: str):
        score = compute_score(response, prompt)

        return {
            "engine_version": self.version,
            "score": score,
            "normalized_score": score / 3,
            "pass": score >= 2
        }