from question import question

question_prompts = [
    "what color is a banana\n(a) yellow\n(b) green\n(c) blue\n\n"
    "what color is a green apple\n(a) yellow\n(b) green\n(c) blue\n\n"
    "what color is the sky\n(a) yellow\n(b) green\n(c) blue\n\n"
]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(question)