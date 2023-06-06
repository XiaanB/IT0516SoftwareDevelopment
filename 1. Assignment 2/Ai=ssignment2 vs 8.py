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
        # self._class_.ticket_list.append(self)

    def create_new_ticket(self):
        # ticket_number += 1

        user_id = input("Please enter your ID:")

    #ticket_list.append(Ticket(ticket_number, userId, 'cbb', 'gtgfgsdfg', 'hard',

                              'none', 'open'))

    #print(ticket_list[ticket_number].ticketNumber)


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


ticket_main_list = []

choice = "-"

ticket_list = []

ticket_number = 2000

choice = input("\nPlease select and option between 1-5:\n")

while choice != "0":

    if choice == "1":
        employee_id = input("Please enter your ID")

        employee_name = input("Please enter your name")

        employee_email = input("Please enter your email")

        emp = Ticket(ticket_number, employee_id, employee_name,

                     employee_email, 'hard',

                     'none', 'open')

        # ticket_list.append(emp)

        # Ticket.create_new_ticket()

        ticket_list.append(Ticket(ticket_number, employee_id, 'cbb', 'gtgfgsdfg', 'hard',

                                  'none', 'open'))

        ticket_main_list.append(Ticket(ticket_list))

        print(*ticket_list)

        print(*ticket_main_list)

        # print(ticket_list[ticket_number])

        ticket_number += 1

        choice = input("\nPlease select and option between 1-5:\n")

    if choice == "2":
        print(ticket_list[ticket_number].ticketNumber)
