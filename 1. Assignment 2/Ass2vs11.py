
number = 200
userList = [[], []]
#tempUserList = []

userName = "-"

while userName != 0:

    userName = input("Please enter your name: ")
    userLastname = input("lastname: ")


    userList[0].append(number)
    userList[1].append(number)
    userList[1].append(userName)
    userList[1].append(userLastname)

    userList.append(userList)
    #userList[0].append(number)

    #print(userList)

    # print(userList)
    # print()
    # print(userList)
    userSelection= input("Would you like to enter another ticket? (y/n) ")
    if userSelection == "y":
        number += 1
        userName = input("Please enter your name: ")
        userLastname = input("lastname: ")

        userList[0].append(number)
        userList[1].append(number)
        userList[1].append(userName)
        userList[1].append(userLastname)
    userList.append(userList)
    #print(userList)
    for r in userList:
        for t in r:
             print(t,)
        print
