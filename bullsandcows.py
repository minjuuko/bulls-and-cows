from random import randint

def answers_generate():
    answers = []
    i = 0
    while i < 4:
        generate = randint(0, 9)
        answers.append(generate)
        i += 1
    return answers

print(answers_generate())
