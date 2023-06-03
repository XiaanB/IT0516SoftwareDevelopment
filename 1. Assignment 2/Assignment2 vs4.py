available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Re-open resolved ticket",
                        "Display ticket state"
                        ]

choice = "-"
ticket_details_dict = {}
ticket_number = 2000
# add ticket response

ticket_status = "Ticket status: " + "Unresolved"
while choice != "0":
    if choice == "1":
        ticket_number += 1
        staff_id = "ID: " + (input("Please enter your staff id."))
        staff_name = "Name: " + input("Please enter you name:")
        staff_email = "Email: " + input("Please enter you email address:")
        print("Do you require a password change?")
        staff_problem = "Problem: " + input("Enter a description of your problem:")
        if staff_problem.lower() == "password change":
            password_user_id = (staff_id[4:6])
            password_user_name = (staff_name[6:9])
            password = password_user_id + password_user_name
            print("Your new password is: ", password)
            ticket_status = "Resolved"
        more_problem = input("Do you have any other problems? Y/N")
        # creating a dict with ticket number as the key and list as the value
        ticket_details_dict[ticket_number] = (staff_id, staff_name, staff_email, staff_problem, ticket_status)
        # fix what happens when user chose Y/N for more problems
    else:
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices: \n")
        for number, selection in enumerate(available_selections):
            print("{0}: {1}".format(number, selection))
        print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")

    # Print all tickets
    if choice == "2":
        for key, values in ticket_details_dict.items():
            print("__________________________________________________")
            print("Ticket Number:", key)
            for i in values:
                print(" : ", i)

    # Respond to a ticket by number
    if choice == "3":
        user_selection = int(input("Please enter the ticket number you wish to see: "))
        for key, values in ticket_details_dict.items():
            print("__________________________________________________")
            if int(key) == user_selection:
                print("Ticket Number:", key)
            if int(key) == user_selection:
                for i in values:
                    print(" : ", i)
                user_choice = input("Would you like to change the status? (Y?N)\n")
                    # if user_choice == "Y":

            # need to find a way to update the ticket status

