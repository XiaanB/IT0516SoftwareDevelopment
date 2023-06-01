# available_selections = ["Exit",
#                         "Submit helpdesk ticket",
#                         "Show all tickets",
#                         "Respond to ticket by number",
#                         "Re-open resolved ticket",
#                         "Display ticket state"
#                         ]
#
# ticket_number = 2000
# ticket_status = "Unresolved"
# choice = "-"
# ticket_details = {'ticket_number': [ticket_number], 'staff_details': []}
# # ticket_detail = []
#
# while choice != "0":
#     # if choice in "12345":
#     #     print("You chose: {}".format(choice))
#     if choice == "1":
#         ticket_number += 1
#         ticket_details[ticket_number] = ticket_number
#         staff_id = (input("Please enter your staff id."))
#         ticket_details = [ticket_number], [staff_id]
#         # ticket_details[ticket_number] = [ticket_details.append(staff_id)]
#         staff_name = input("Please enter you name:")
#         ticket_details = [ticket_number],[staff_name]
#         #ticket_details[ticket_number].append(staff_name)
#         staff_email = input("Please enter you email address:")
#         ticket_details = [ticket_number], [staff_email]
#         print(ticket_details)
#         print("Do you require a password change?")
#         problem = input("Enter a description of your problem.")
#         ticket_details["ticket_detail"].append(problem)
#         if problem.lower() == "password change":
#             password_user_id = (staff_id[0:2])
#             password_user_name = (staff_name[0:3])
#             password = password_user_id + password_user_name
#             print("Your new password is: ", password)
#             ticket_status == "Resolved"
#             ticket_details["ticket_detail"].append(ticket_status)
#         more_problem = input("Do you have any other problems? Y/N")
#         if more_problem == "N":
#             exit()
#     else:
#         print("IT5014 Helpdesk Ticketing System:")
#         print("_______________________________________________________")
#         print("Select one of the following choices:")
#         for number, selection in enumerate(available_selections):
#             print("{0}: {1}".format(number, selection))
#         print("_______________________________________________________")
#
#     choice = input("Please select an option between 0-5:\n")
#
#     if choice == "2":
#         print(ticket_details)
#

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
