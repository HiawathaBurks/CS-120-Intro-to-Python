def main():
    #Dictionary to store Name and Email addresses
    lookup = dict()
    while True: #Loops until 5 is entered
        choice = int(input("\nMENU\nPlease enter your choice:\n""1. Email lookup\n"
                        "2. Add new email\n3. Change existing email\n"
                        "4. Delete email\n5. Exit\n=> "))
        #Print email id of the person
        if choice == 1:
            name = input("Enter the name: ")
            try:
            print("Email of",name, "is: ", lookup[name])
         except KeyError:
            print("Name not found!")
        #Adds new names and email Id to the dictionary
        if choice == 2:
            name = input("Enter new Name: ")
            email = input("Enter email: ")
            lookup[name] = email
        #Edit email of a certain name
        if choice == 3:
            name = input("\nEnter the name you want to edit: ")
            email = input("Enter the new email: ")
            try:
                lookup[name] = eid
            except KeyError:
            print("Name not found!")
        #Deletes record of a certain name
        if choice == 4:
            name = input("\nEnter the name you want to delete: ")
            try:
                lookup.pop(name, None)
            except KeyError:
            print("Name not found!")
        #Exits the program
        if choice == 5:
            break

main()

#End of program
