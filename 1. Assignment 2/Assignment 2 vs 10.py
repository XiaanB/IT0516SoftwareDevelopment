ticket_details = {'ticket_number': ['userId', 'userName']}
ticketNumber = 2000


menu = {'1': "Add ticket.", '2': "Delete Student.", '3': "Find Student", '4': "Exit"}

while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select:\n")
    if selection == '1':
        ticketNumber += 1
        print("add")
        print("Enter First name, last name and Student ID number. Then press 0 to continue")
        userFirst = str(input("Enter First Here:"))
        userLast = str(input("Enter Last Name:"))
        userStudent = int(input("Enter Student ID number:"))
        userInfo = input("Enter more details or pres 0 to enter search mode")

        # Changed SearchMode to be nested list with each list Holding the input values from
        # [ [UserFirst],[userLast],[userStudent] ]
        searchMode = [[], []]
        # Append userFirst to the first Indexed List
        searchMode.append(ticketNumber)

        searchMode.append(userStudent)
        # Append userLast to the second Indexed List
        searchMode.append(userLast)
        # Append userStudent to the third Indexed List
        searchMode.append(userFirst)

        userSearch = int(input("Enter ticket number"))

        # Since we know that we need to search by The Student Id we Take the InitialList and add the index of our
        # desired
        # Nested List; In this Case it's the 3rd nested
        # Then we take the values from the nested List and look for the inputted value and obtain the record
        # corresponding index
        for i in range(0, len(searchMode)):
            print(searchMode[i])
        print(searchMode)
        userSearch = searchMode[0]
        print(userSearch)
        # for list in searchMode:
        #     for number in list:
        #         print(number, end=' ')

    elif selection == '2':
        print("delete")
    elif selection == '3':
        print("find")
    elif selection == '4':
        break
    else:
        print("Unknown Option Selected!")

ans = input("What would you like to do?")

