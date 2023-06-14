#I have not defined any def's to optimize the code and get rid of repeating code.

#Menu for selecting the optiosn on the ticket.
available_selections = ["Exit",
                        "Submit helpdesk ticket",
                        "Show all tickets",
                        "Respond to ticket by number",
                        "Ticket stats",
                        "Re-open resolved ticket",
                        ]
#Printing a nice welcome sreen for the user to make a selection
print("IT5014 Helpdesk Ticketing System:")
print("_______________________________________________________")
print("Select one of the following choices: \n")

for number, selection in enumerate(available_selections):
    print("{0}: {1}".format(number, selection))
print("_______________________________________________________")

#User get a chance to make a selection based on the above options. No error handeling yet.
choice = input("\nPlease select and option between 0-5:\n")

#creating an empty list to store user and ticket data. This will be a bested list.
ticketList = []
#From the above selections, if the user select 0 the program will terminate. Once again no error handeling, assuming the user will allways select the correct option.
while choice != "0":
    if choice == "1":
        #Ticket number starts at 2000
        number = 2000
        userInput = "-"
        userInput = input("Raise another ticket: (y/n) \n")
        while userInput != "-":
            #Creating a temp list to store each ticket and user data in. This will update the nested list each time option 1 is selected.
            tempList = []
            number += 1
            employeeId = input("Enter your ID: ")
            employeeName = input("Enter your name: ")
            employeeLastName = input("Lastname: ")
            employeeEmail = input("Enter your email address: ")
            employeeIssue = input("Enter a description of your problem: \n")
            ticketStatus = "Open"
            ticketResponse = "Not Yet Provided"

            tempList.append(number)
            tempList.append(employeeId)
            tempList.append(employeeName)
            tempList.append(employeeLastName)
            tempList.append(employeeEmail)
            tempList.append(employeeIssue)
            tempList.append(ticketStatus)
            tempList.append(ticketResponse)

            #OPtion to generate a new password and to change the ticket status and ticker response
            if employeeIssue == "password change":
                passwordUserId = (employeeId[0:2])
                passwordUserName = (employeeName[0:3])
                password = passwordUserId + passwordUserName
                print("Your new password is: ", password)
                tempList[6] = "Closed"
                tempList[7] = "New password generated"
            ticketList.append(tempList)
            # if (y) the option 1 is repeated and a new ticket with a new number is created. No error handleing yet.
            userInput = input("Raise another ticket: (y/n/-) \n")
            if userInput == "n":
                print("IT5014 Helpdesk Ticketing System:")
                print("_______________________________________________________")
                print("Select one of the following choices: \n")

                for number, selection in enumerate(available_selections):
                    print("{0}: {1}".format(number, selection))
                print("_______________________________________________________")

                choice = input("\nPlease select and option between 0-6:\n")

                #Looping throught the nested list and printing
                if choice == "2":
                    for r in ticketList:
                        print("Ticket Number: ")
                        for t in r:
                            print(t,)
                        print()
                choice = input("\nPlease select and option between 0-5:\n")
                if choice == "0":
                    break

                    #enumerating through the list and looking for the ticket number the user entered.
                    #once found the IT user can give a response and the ticket will close automatically
                if choice == "3":
                    for (i, item) in enumerate(ticketList, start=0):
                        print(i, item)
                    ticket_number = int(input("Please enter the ticket number you wish to edit: \n"))
                    print(any(ticket_number in inner_list for inner_list in ticketList))

                    for sub_list in ticketList:
                        if ticket_number in sub_list:
                            print(ticketList.index(sub_list), sub_list.index(ticket_number))
                            #print(ticketList[ticketList.index(sub_list)])

                            itResponse = input("Please respond:")

                            ticketList[ticketList.index(sub_list)][6] = "Closed"
                            ticketList[ticketList.index(sub_list)][7] = itResponse
                            print(ticketList[ticketList.index(sub_list)])

                            print("Ticket Number: ")
                            print(ticketList[ticketList.index(sub_list)][sub_list.index(ticket_number)])
                            print()
                            for r in ticketList:
                                print("Ticket Number: ")
                                for t in r:
                                    print(t,)
                                print()
                            else:
                                print("IT5014 Helpdesk Ticketing System:")
                                print("_______________________________________________________")
                                print("Select one of the following choices: \n")

                                for number, selection in enumerate(available_selections):
                                    print("{0}: {1}".format(number, selection))
                                print("_______________________________________________________")

                            choice = input("\nPlease select and option between 0-6:\n")

                    #enumerating through the list and looking for the ticket number the user entered.
                    #once found the IT user can give a response and the ticket will open automatically
                if choice == "4":
                    openTicketsCounter = 0
                    closedTicketCounter = 0

                    for sub_list in ticketList:
                        if "Open" in sub_list:
                            openTicketsCounter += 1

                    for sub_list in ticketList:
                        if "Closed" in sub_list:
                            closedTicketCounter += 1

                    print("open tickets")
                    print(openTicketsCounter, "\n")
                    print("closed tickets")
                    print(closedTicketCounter, "\n")
                    print("tickets to be closed")
                    print((openTicketsCounter + closedTicketCounter) - openTicketsCounter)

                #Enumerating over the lists and looking for the word "open"and "closed". Each time one is found it adds 1 to the appropriate variable
                if choice == "5":
                    for (i, item) in enumerate(ticketList, start=0):
                        print(i, item)
                    ticket_number = int(input("Please enter the ticket number you wish to edit: \n"))
                    print(any(ticket_number in inner_list for inner_list in ticketList))

                    for sub_list in ticketList:
                        if ticket_number in sub_list:
                            print(ticketList.index(sub_list), sub_list.index(ticket_number))
                            #print(ticketList[ticketList.index(sub_list)])

                            itResponse = input("Please give a reasonfor opening up the ticket:")

                            ticketList[ticketList.index(sub_list)][6] = "Open"
                            ticketList[ticketList.index(sub_list)][7] = itResponse
                            print(ticketList[ticketList.index(sub_list)])

                            print("Ticket Number: ")
                            print (ticketList[ticketList.index(sub_list)][sub_list.index(ticket_number)])
                            print()
                            for r in ticketList:
                                print("Ticket Number: ")
                                for t in r:
                                    print(t,)
                                print()