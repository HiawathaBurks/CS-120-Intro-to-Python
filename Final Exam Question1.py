def menu():
    while True:
        userChoice = int(input("\n MENU \nPlease Enter your Choice: \n 1.Enter a Name"
                               "\n 2.Quit \n"))
        if userChoice == 1:
            searchForName()

        if userChoice == 2:
            break;
    
def searchForName():
    file = open('GirlNames.txt')
    nameSearch = file.read()
    searchName = input("Enter a Name to search: ")
    print("\n")
    if searchName in nameSearch:
        print(searchName, "is amoung the most popular names.")
    else:
        print(searchName, "is NOT amoung the most popular names.")
            
def main():
    menu()



main()
