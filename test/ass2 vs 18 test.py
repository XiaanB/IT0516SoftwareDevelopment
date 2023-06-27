


# Create class "Student"
class Ticket:
    # Initial ticket number
    ticket_count = 2000
    def __init__(self, ticket_number, user_id, first_name, last_name, email_address, description_of_the_issue,
                 ticket_status, it_response):
        self.number = ticket_number
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.Description_of_the_issue = description_of_the_issue
        self.status = ticket_status
        self.it_response = it_response

    # Function to create and append new student
    def new_ticket(self, number, user_id, first_name, last_name, email_address, description_of_the_issue, status,
                   it_response):
        ob = Ticket(number, user_id, first_name, last_name, email_address, description_of_the_issue, status,
                    it_response)
        ticket_list.append(ob)

    def search(self, ticket_number):
        for i in range(ticket_list.__len__()):
            if ticket_list[i].number == ticket_number:
                return i

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


# Create a list to add Students
ticket_list = []

# an object of Student class
obj = Ticket('', 0, 0, 0, 0, 0, 0, 0)
print("\nOperations used, ")

number = 2000


def password_change_method():
    global status, it_response
    password_user_id = user_id[0:2]
    password_user_name = name[0:3]
    password = password_user_id + password_user_name
    print("Your new password is: ", password)
    status = "Closed"
    it_response = "New password generated"


while True:
    print(
        "\n1 -- Enter ticket Details\n2 -- Display All Ticket Details\n3 -- Search for a specific ticket\n"
        "4 -- IT response and close ticket\n5 -- Ticket Stats\n6 -- Open closed ticket\n7 -- Exit\n")
    try:
        user_selection = int(input("Enter choice (1 - 7): \n"))
    except ValueError:
        print("Invalid input. Enter a value between 1 - 7. ")
    number += 1
    if user_selection == 1:
        user_id = input("Enter your ID: ")
        name = input("Enter your Name: ")
        last_name = input("Enter your Last name: ")
        email = input("Enter your Email address: ")
        problem = input("Enter your Description of the issue : ")
        status = "Open"
        it_response = "Not Yet Provided"
        if problem.lower() == "password change":
            password_change_method()

        obj.new_ticket(number, user_id, name, last_name, email, problem, status, it_response)

    elif user_selection == 2:
        print("\n")
        print("\nList of Tickets\n")

        for i in range(ticket_list.__len__()):
            obj.display(ticket_list[i])

    elif user_selection == 3:
        search_number = int(input("Enter the ticket number to search for: "))
        s = obj.search(search_number)
        obj.display(ticket_list[s])

    elif user_selection == 4:
        search_number_update = int(input("Enter the ticket number to close: "))
        s = obj.search(search_number_update)
        ticket_list[s].status = "Closed"
        ticket_list[s].it_response = input("Please enter a reason: ")
        obj.display(ticket_list[s])

    elif user_selection == 5:
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

        print("Tickets created  : ", (open_tickets_counter + closed_ticket_counter +
                                      reopened_ticket_counter))
        print("Tickets to solve : ", open_tickets_counter)
        print("Tickets resolved : ", closed_ticket_counter)
        print("Tickets re-opened: ", reopened_ticket_counter)

    elif user_selection == 6:
        search_number_update = int(input("Enter the ticket number to re-open: "))
        s = obj.search(search_number_update)
        ticket_list[s].status = "Reopened"
        ticket_list[s].it_response = input("Please provide a reason for opening this ticket: \n")
        obj.display(ticket_list[s])

    elif user_selection == 7:
        exit()

    else:
        print("Thank You !")
