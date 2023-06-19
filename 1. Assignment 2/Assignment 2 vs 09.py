ticket_details = {'ticket_number': ['userId', 'userName']}


menu = {'1': "Add Student.", '2': "Delete Student.", '3': "Find Student", '4': "Exit"}

while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select:")
    if selection == '1':
        print("add")
    elif selection == '2':
        print("delete")
    elif selection == '3':
        print("find")
    elif selection == '4':
        break
    else:
        print("Unknown Option Selected!")

ans = input("What would you like to do?")
