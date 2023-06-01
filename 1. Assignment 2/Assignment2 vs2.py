choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose: {}".format(choice))
    else:
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices:")
        print("1:\tSubmit helpdesk ticket")
        print("2:\tShow all tickets")
        print("3:\tRespond to ticket by number")
        print("4:\tRe-open resolved ticket")
        print("5:\tDisplay ticket state")
        print("0:\tExit")
        print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")


