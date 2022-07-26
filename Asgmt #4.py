#Q1
def magicSquare(matrix):
    size = len(matrix[0])

    #initialise the list for the matrix
    lst = []

    #for loop for vertical angle
    for c in range(size):
        lst.append(sum(r[c] for r in matrix))

    #set the horizontal value
    lst.extend([sum (lines) for lines in matrix])
    rst = 0

    for i in range(0,size):

        rst +=matrix[i][i]

    lst.append(rst)   
    d_rst = 0

    #finds the result
    for i in range(size-1,-1,-1):

        d_rst +=matrix[i][i]

    lst.append(d_rst)

    #check the length of the list to determine if its a magic square
    if len(set(lst))>1:
        return print(matrix,'is not a magic square')

    else:
        return print(matrix,'is a magic square')

#Q2
def function1():

    file = open("number_list.txt","w")
    for x in range(1,6):
       file.write(str(x)+"\n")
    file.close()

def function2():
    
    sum=0
    with open("number_list.txt") as f:
        for x in f:
            sum=sum+int(x)
    print("Sum of numbers: ",sum)

def function3():

    file = open("number_list.txt",'a')
    for x in range(6, 11):
        file.write(str(x)+"\n")
    file.close()

#calls the all functions
def main():
    magicSquare([[4,9,2], [3,5,7], [8,1,6]])
    magicSquare([[2,7,6], [9,5,1], [4,3,8]])
    magicSquare([[1,2,3], [4,5,6], [7,8,9]])
    magicSquare([[4,9,2], [3,5,5], [8,1,6]])
    function1()
    function2()
    function3()

main()
