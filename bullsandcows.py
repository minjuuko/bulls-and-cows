# 좌훈님
from random import randint

def answers_generate():
    answers = []
    i = 0
    while i < 4:
        generate = randint(0, 9)
        if(generate not in answers):
            answers.append(generate)
            i += 1
    return answers

#print(answers_generate())


# 민주님
import random

num = list(range(0,10))
answer = []
for i in range(4):
     answer.append(num.pop(num.index(random.choice(num))))
