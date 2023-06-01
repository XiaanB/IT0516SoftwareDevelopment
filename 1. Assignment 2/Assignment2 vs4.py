available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Re-open resolved ticket",
                        "Display ticket state"
                        ]

ticket_number = 2000
ticket_status = "Unresolved"
choice = "-"
ticket_details_dict = {}

while choice != "0":
    if choice == "1":
        ticket_number += 1
        staff_id = "ID: " + (input("Please enter your staff id."))
        staff_name = "Name: " + input("Please enter you name:")
        staff_email = "Email: " + input("Please enter you email address:")
        print("Do you require a password change?")
        staff_problem = input("Enter a description of your problem:")
        if staff_problem.lower() == "password change":
            password_user_id = (staff_id[4:6])
            password_user_name = (staff_name[6:9])
            password = password_user_id + password_user_name
            print("Your new password is: ", password)
            ticket_status = "Resolved"
        more_problem = input("Do you have any other problems? Y/N")
        ticket_details_dict[ticket_number] = (staff_id, staff_name, staff_email, staff_problem, ticket_status)
        if more_problem == "N":
            for key, values in ticket_details_dict.items():
                print("Ticket Number:", key)
                for i in values:
                    print( " : ", i)
            exit()
    else:
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices:")
        for number, selection in enumerate(available_selections):
            print("{0}: {1}".format(number, selection))
        print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")

    if choice == "2":
        print(ticket_details_dict)
