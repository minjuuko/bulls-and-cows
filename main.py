import random

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    numList = getDigits(num)
    if (len(numList) == len(set(numList))):
        return True
    else:
        return False

def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num

num = generateNum()
print(num)