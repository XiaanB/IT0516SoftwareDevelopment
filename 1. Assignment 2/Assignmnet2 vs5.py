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

ticket_details_nested_lest = [[], []]
ticket_number = 2000
choice = "-"

# employee_id = ""
# employee_name = ""
# employee_email = ""
# employee_issue = ""
# ticket_status = ""
# ticket_response = ""
#
# ticket_details_nested_lest = [[ticket_number], [employee_id, employee_name, employee_email, employee_issue,
#                                                 ticket_status, ticket_response]]

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
        ticket_details_nested_lest = [[ticket_number].append(ticket_number), [employee_id, employee_name, employee_email, employee_issue,
                                                        ticket_status, ticket_response]]
    else:
        print("IT5014 Helpdesk Ticketing System:")
        print("_______________________________________________________")
        print("Select one of the following choices: \n")
        for number, selection in enumerate(available_selections):
            print("{0}: {1}".format(number, selection))
        print("_______________________________________________________")

    choice = input("Please select an option between 0-5:\n")

    if choice =="2":
        print(ticket_details_nested_lest)