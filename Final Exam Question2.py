import random

def guessNumber(userAns, correctAns):
    if userAns == correctAns:
        print("Congradulations! You got the right answer.")
    else:
        print("Answer incorrect. The ight answer is ",correctAns)

def equation():
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    print("Answer the following question: \n")
    print(number1, " + ",number2, " = \n")
    userAnswer = int(input("Your Answer: "))
    correctAnswer = number1 + number2
    guessNumber(userAnswer, correctAnswer)
def main():
    equation()

main()
    
