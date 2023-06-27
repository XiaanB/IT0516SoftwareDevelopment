import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# Create class "Student"
class Ticket:

    def __init__(self, ticket_number, user_ids, first_names, last_names, email_address, description_of_the_issue,
                 ticket_status, it_responses):
        self.number = ticket_number
        self.user_id = user_ids
        self.first_name = first_names
        self.last_name = last_names
        self.email_address = email_address
        self.Description_of_the_issue = description_of_the_issue
        self.status = ticket_status
        self.it_response = it_responses

    # Function to create and append new student
    def new_ticket(self, numbers, user_ids, first_name, last_names, email_address, description_of_the_issue, statuses,
                   it_responses):
        ob = Ticket(numbers, user_ids, first_name, last_names, email_address, description_of_the_issue, statuses,
                    it_responses)
        ticket_list.append(ob)

    def search(self, ticket_number):
        for j in range(ticket_list.__len__()):
                if ticket_list[j].number == ticket_number:
                    return j


    # Function to display student details
    def display(self, ob):
        print("Number: ", ob.number)
        print("Id : ", ob.user_id)
        print("Name : ", ob.first_name)
        print("LastName : ", ob.last_name)
        print("Email : ", ob.email_address)
        print("Description : ", ob.Description_of_the_issue)
        print("Status : ", ob.status)
        print("IT response: ", ob.it_response)
        print("\n")

    def password_change_method(self):
        global status, it_response
        password_user_id = user_id[0:2]
        password_user_name = name[0:3]
        password = password_user_id + password_user_name
        print("Your new password is: ", password)
        status = "Closed"
        it_response = "New password generated"

    def ticket_stats(self):
        global i
        open_tickets_counter = 0
        closed_ticket_counter = 0
        reopened_ticket_counter = 0
        for i in range(ticket_list.__len__()):
            if ticket_list[i].status == "Open":
                open_tickets_counter += 1
        for i in range(ticket_list.__len__()):
            if ticket_list[i].status == "Closed":
                closed_ticket_counter += 1
        for i in range(ticket_list.__len__()):
            if ticket_list[i].status == "Reopened":
                reopened_ticket_counter += 1
        total_tickets = open_tickets_counter + closed_ticket_counter + reopened_ticket_counter
        percentage_closed = ((closed_ticket_counter/total_tickets)*100)
        percentage_open = ((open_tickets_counter/total_tickets)*100)
        percentage_rework = ((reopened_ticket_counter/total_tickets)*100)
        print("Tickets created  : ", total_tickets)
        print("Tickets to solve : ", open_tickets_counter, percentage_open)
        print("Tickets resolved : ", closed_ticket_counter, percentage_closed)
        print("Tickets re-opened: ", reopened_ticket_counter, percentage_rework)


# an object of Student class
obj = Ticket('', 0, 0, 0, 0, 0, 0, 0)

# Create a list to add Students
ticket_list = []
ticket_open_new_counter = 0
ticket_closed_new_close_counter = 0
number = 2000


def menu():
    print(
        "\nIT5014 Helpdesk Ticketing System:\n"
        "_______________________________________________________"
        "\n1 -- Enter ticket Details\n2 -- Display All Ticket Details\n3 -- Search for a specific ticket\n"
        "4 -- IT response and close ticket\n5 -- Ticket Stats\n6 -- Open closed ticket\n7 -- Exit\n"
        "_______________________________________________________"
    )


def search_validation():
    global search_number
    while True:
        try:
            search_number = int(input("Enter the ticket number to search for: "))
            break
        except ValueError:
            print("This not a valid ticket number...")
            continue


while True:
    menu()
    user_selection = " "
    try:
        user_selection = int(input("Enter choice (1 - 7): \n"))
    except ValueError:
        print("Invalid input. Enter a value between 1 - 7. ")
    number += 1
    if user_selection == 1:
        user_id = input("Enter your ID: ")
        while True:
            name = input("Enter your Name: ")
            if len(name) > 2 and name != "":
                break
            else:
                print("Please enter a valid name...")
        while True:
            last_name = input("Enter your Last name: ")
            if len(last_name) > 2 and last_name != "":
                break
            else:
                print("Please enter a valid last name...")
        while True:
            email = input("Enter your Email address: ")
            if re.search(regex, email):
                break
            else:
                print("Invalid email address, Please enter a valid email address...")
        while True:
            problem = input("Enter your Description of the issue: ")
            if len(problem) != "":
                break
            else:
                print("Please enter a valid description of your issue...")
        status = "Open"
        it_response = "Not Yet Provided"
        if problem.lower() == "password change":
            obj.password_change_method()
            ticket_closed_new_close_counter += 1

        obj.new_ticket(number, user_id, name, last_name, email, problem, status, it_response)
        ticket_open_new_counter +=1

    elif user_selection == 2:
        print("\n")
        print("\nList of Tickets\n")

        for i in range(ticket_list.__len__()):
            obj.display(ticket_list[i])

    elif user_selection == 3:
        search_validation()
        try:
            s = obj.search(search_number)
            obj.display(ticket_list[s])
        except TypeError:
            print("Ticket number not in the list, start again...")


    elif user_selection == 4:
        search_validation()
        try:
            s = obj.search(search_number)
            ticket_list[s].status = "Closed"
            ticket_list[s].it_response = input("Please enter a reason: ")
            obj.display(ticket_list[s])
            ticket_closed_new_close_counter += 1
            ticket_open_new_counter -= 1
        except TypeError:
            print("Ticket number not in the list, start again...")


    elif user_selection == 5:
        #obj.ticket_stats()
        print("open", ticket_open_new_counter)
        print("closed", ticket_closed_new_close_counter)

    elif user_selection == 6:
        search_validation()
        try:
            s = obj.search(search_number)
            obj.display(ticket_list[s])
            ticket_list[s].status = "Reopened"
            original_it_response = ticket_list[s].it_response
            ticket_list[s].it_response = original_it_response, input("Please provide a reason for opening this "
                                                                     "ticket: \n")
            obj.display(ticket_list[s])
            ticket_open_new_counter += 1
            ticket_closed_new_close_counter -= 1
        except TypeError:
            print("Ticket number not in the list, start again...")


    elif user_selection == 7:
        exit()

    else:
        print("Thank You !")
