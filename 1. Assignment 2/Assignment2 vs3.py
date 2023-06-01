available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Re-open resolved ticket",
                        "Display ticket state"
                        ]
choice = "-"
while choice != "0":
    # if choice in "12345":
    #     print("You chose: {}".format(choice))
    if choice == "1":
        ticket_details = []
        staff_id = int(input("Please enter your staff id."))
        ticket_details.append(staff_id)
        staff_name = input("Please enter you name:")
        ticket_details.append(staff_name)
        staff_email = input("Please enter you email address:")
        ticket_details.append(staff_email)
        print(ticket_details)
        print("Do you require a password change?")
        problem = input("Enter a description of your problem.")
        if problem == "Password change":
            print("to be done")
    else:
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices:")
        for number, selection in enumerate(available_selections):
            print("{0}: {1}".format(number, selection))
        print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")

# if choice == 1:                                                  
#     # ticket_counter = 0
#     # ticketDetails = {"ticket_number": ["staff_id", "staff_name ", "staff_email", "staff_password", "ticked_status"]}
#     ticket_details = []
#     print("\n")
#     staff_id = int(input("Please enter your staff id."))
#     ticket_details.append(staff_id)
#     staff_name = input("Please enter you name:")
#     ticket_details.append(staff_name)
#     staff_email = input("Please enter you email address:")
#     ticket_details.append(staff_email)
#     print(ticket_details)
#
