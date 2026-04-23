def evaluate(prompt, response):
    score = 0

    if len(response) > 80:
        score += 1

    if any(word in response.lower() for word in prompt.lower().split()):
        score += 1

    if "." in response:
        score += 1

    return {
        "score": score,
        "max": 3
    }