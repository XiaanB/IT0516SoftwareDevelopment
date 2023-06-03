available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Re-open resolved ticket",
                        "Display ticket state"
                        ]
print("IT5014 Helpdesk Ticketing System:")
print("_______________________________________________________")
print("Select one of the following choices: \n")
for number, selection in enumerate(available_selections):
    print("{0}: {1}".format(number, selection))
print("_______________________________________________________")

employee_id = ""
employee_name = ""
employee_email = ""
employee_issue = ""
ticket_status = ""
ticket_response = ""

ticket_number = 2000
choice = "-"
ticket_details_nested_dict = {}
# ticket_details_nested_dict = {ticket_number: {'ID': employee_id, 'Name': 'employee_name', 'Email': 'employee_email',
#                                               'Issue': 'employee_issue', 'Ticket status': 'ticket_status',
#                                               'Ticket response': 'ticket_response'}}

while choice != "0":
    if choice == "1":
        ticket_number += 1
        employee_id = input("Please enter your staff id.")
        employee_name = input("Please enter you name:")
        employee_email = input("Please enter you email address:")
        print("Do you require a password change?")
        employee_issue = input("Enter a description of your problem:")
        if employee_issue == "password change":
            password_user_id = (employee_id[0:2])
            password_user_name = (employee_name[0:3])
            password = password_user_id + password_user_name
            print("Your new password is: ", password)
            ticket_status = "Resolved"
            ticket_response = "Problem solved"
        ticket_status = "Unresolved"
        ticket_response = ""
        more_problem = input("Do you have any other problems? Y/N ")
        ticket_details_nested_dict[ticket_number] = {'ID': employee_id, 'Name': employee_name,
                                                     'Email': employee_email,
                                                     'Issue': employee_issue, 'Ticket status': ticket_status,
                                                     'Ticket response': ticket_response}
    # else:
    #     print("IT5014 Helpdesk Ticketing System:")
    #     print("_______________________________________________________")
    #     print("Select one of the following choices: \n")
    #     for number, selection in enumerate(available_selections):
    #         print("{0}: {1}".format(number, selection))
    #     print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")

    if choice == "2":
        for key, values in ticket_details_nested_dict.items():
            print("__________________________________________________")
            print("Ticket Number:", key)
            for i in values:
                print(" : ", i)
            print(ticket_details_nested_dict.items())

    if choice == "3":
        ticket_number = int(input("Please enter the ticket number you wish to edit: \n"))
        keys = ticket_number
        print(ticket_details_nested_dict[keys])
        employee_name = "John"
        ticket_details_nested_dict[keys]['Name'] = employee_name
        ticket_details_nested_dict[keys]['Ticket status'] = "resolved"
        user_rsponse = input("Please enter your response: \n")
        ticket_details_nested_dict[keys]['Ticket_response'] = user_rsponse
        print("All done")
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices: \n")
        for number, selection in enumerate(available_selections):
            print("{0}: {1}".format(number, selection))
        print("_______________________________________________________")
