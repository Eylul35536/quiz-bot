def ask_question(question: str, answer: str) -> bool:
    user_answer = input(question + " ")
    return user_answer.strip().lower() == answer.lower()


def run_quiz():
    questions = [
        ("Sky what color?", "blue"),
        ("2 + 2 =", "4"),
    ]

    score = 0

    for q, a in questions:
        if ask_question(q, a):
            score += 1

    return score

def get_questions():
    return []
