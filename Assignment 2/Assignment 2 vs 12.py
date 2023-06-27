userList = []
number = 2000

userInput = "-"
userInput = input("Raise another ticket: (y/n) \n")
while userInput != "-":
    tempList = []
    number += 1
    name = "Name: " + input("Enter your name: ")
    lastName ="Last Name: " + input("Lastname?: ")

    tempList.append(number)
    tempList.append(name)
    tempList.append(lastName)
    userList.append(tempList)
    userInput = input("Raise another ticket: (y/n) \n")
    if userInput == "n":
        for r in userList:
            print("Ticket Number: ")
            for t in r:
                print(t,)
            print()
