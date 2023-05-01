import random

num = list(range(0,10))
answer = []
for i in range(4):
     answer.append(num.pop(num.index(random.choice(num))))
