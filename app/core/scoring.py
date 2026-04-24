def compute_score(response: str, prompt: str):
    score = 0

    if len(response) > 100:
        score += 1

    if any(word in response.lower() for word in prompt.lower().split()):
        score += 1

    if response.endswith("."):
        score += 1

    return score