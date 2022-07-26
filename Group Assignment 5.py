#Group Assignment 5 by Hiawatha B
#Q1
def times_ten(num):
    multiply = num * 10
    print(num,'times 10 is',multiply)

#Q2
def my_function(a, b, c):
    d = (a + c)/b
    print(d)

#Q3
def main():
    Calories1 = int(input('How many calories are in the first food?'))
    Calories2 = int(input('How many calories are in the second food?'))
    showCalories(Calories1, Calories2)

def showCalories(calories1, calories2):
    print('The total calories you ate today', format(calories1 + calories2, '.2f'))

#Q4
def askUser():
    loanPay = int(input('How much is the monthly loan payment?'))
    insurance = int(input('How much is the monthly insurance?'))
    gas = int(input('How much is the monthly gas?'))
    oil = int(input('How much is the monthly oil??'))
    tires = int(input('How much is the monthly tires?'))
    maintenance = int(input('How much is the monthly maintenance?'))
    showExpenses(loanPay, insurance, gas, oil, tires, maintenance)

def showExpenses(loanPay, insurance, gas, oil, tires, maintenance):
    totalMonthly = loanPay + insurance + gas + oil + tires + maintenance
    print('The total Monthly expenses:',format(totalMonthly, '.2f'))
    yearly = totalMonthly * 12
    print('The total Yearly expenses:',format(yearly, '.2f'))

#Calls all questions
def callAllFunctions():
    times_ten(5)
    #Q2 i
    my_function(2,4,6) #Q2 ii The output should be 2.0 since it dividing
    main()
    askUser()
    
    

callAllFunctions()
