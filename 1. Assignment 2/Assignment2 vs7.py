class Ticket:

    def __init__(self, ticketNumber, userId, userName, userEmail,
                 descriptionOfIissue, responseFromIt, ticketStatus):
        self.ticketNumber = ticketNumber
        self.userId = userId
        self.userName = userName
        self.userEmail = userEmail
        self.descriptionOfIissue = descriptionOfIissue
        self.responseFromIt = responseFromIt
        self.ticketStatus = ticketStatus
        #self._class_.ticket_list.append(self)

available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Re-open resolved ticket",
                        "Display ticket state"
                        ]
# print("IT5014 Helpdesk Ticketing System:")
# print("_______________________________________________________")
# print("Select one of the following choices: \n")
# for number, selection in enumerate(available_selections):
#     print("{0}: {1}".format(number, selection))
# print("_______________________________________________________")

ticket_main_list =[]
choice = "-"
ticket_list = []
ticket_number = 2000
choice = input("\nPlease select and option between 1-5:\n")

while choice != "0":
    if choice == "1":
        ticket_number += 1
        user_id = input("Please enter your ID:")
        ticket_list.append(Ticket(ticket_number, user_id, 'cbb', 'gtgfgsdfg', 'hard',
                                  'none', 'open'))
        ticket_number = ticket_number + 1
    print(ticket_list[0].ticketNumber)
    for obj in ticket_list:
        print(obj.userId, obj.ticketStatus, sep=' ')
        print(ticket_list[0].ticketNumber)
    print(ticket_main_list[0])

else:
    print("IT5014 Helpdesk Ticketing System:")
    print("_______________________________________________________")
    print("Select one of the following choices: \n")

    for number, selection in enumerate(available_selections):
        print("{0}: {1}".format(number, selection))
    print("_______________________________________________________")

    choice = input("\nPlease select and option between 1-5:\n")
    ticket_main_list.append(ticket_list)

if choice == "2":
    print(ticket_list[0].ticketNumber)