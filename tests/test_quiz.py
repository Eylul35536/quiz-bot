from src.quiz import get_questions

def test_get_questions_returns_list():
    questions = get_questions()
    assert isinstance(questions, list)
