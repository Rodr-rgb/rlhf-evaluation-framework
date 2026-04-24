from app.core.scoring import compute_score

def test_scoring():
    result = compute_score("hello world", "hello world.")
    assert result >= 1