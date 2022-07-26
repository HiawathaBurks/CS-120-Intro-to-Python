#Code created by Hiaweatha B
#Q1
import random

RANDOM_NUMBER_LIST = [random.randint(0,1000)]

def isEven(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

def randomNum():
    evenCounter = 0
    oddCounter = 0
    randomNumbers = []
    for i in range(100):
        num = random.randint(0,100)
        randomNumbers.append(num)
    for x in range(99):
        y = randomNumbers[x]
        isEven(y)
        if(isEven(y) == 1):
            evenCounter += 1
        else:
            oddCounter += 1
    print('The total amount of even numbers is', evenCounter)
    print('The total amount of odd numbers is', oddCounter)

randomNum()

print('End of Program')
