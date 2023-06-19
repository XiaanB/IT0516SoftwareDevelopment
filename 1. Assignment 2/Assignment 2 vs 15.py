# creating a class to capture user details
class UserDetails:
    ticket_number = 2000

    def __init__(self,user_id, first_name, last_name, email_address, description_of_problem):
        self.user_id = input("Enter your ID: ")
        self.firs_name = input("Enter your name: ")
        self.last_name = input("Please enter your lastname: ")
        self.email_address = input("Enter your email address: ")
        self.description_of_problem = input("Enter a description of your problem: \n")
        UserDetails.ticket_number += 1


    def show_all_tickets(self):
        print("User ID:", self.user_id, "First Name:", self.firs_name,
              "Last Name:", self.last_name, "Email Address:", self.email_address, "Problem description:",
              self.description_of_problem)



# def change_password():
    #   Option to generate a new password and to change the ticket status and ticker response
    #   if UserDetails(description_of_problem=) == "password change":
    #     passwordUserId = UserDetails(user_id=)[0:2]
    #     passwordUserName = UserDetails([0:3])
    #     password = passwordUserId + passwordUserName
    #     print("Your new password is: ", password)
    #     temp_list[6] = "Closed"
    #     temp_list[7] = "New password generated"
    # ticketList.append(temp_list)


def print_menu():
    print("IT5014 Helpdesk Ticketing System:")
    print("_______________________________________________________")
    print("Select one of the following choices: \n")

    for key in available_selections.keys():
        print(key, '--', available_selections[key])
    print("_______________________________________________________")


def exit_program():
    print('Thank you for using the IT ticketing program.')
    exit()


def change_password():


    pass
def submit_helpdesk_ticket():
    ticket_list = []
    number = 2000
    user_input = input("Raise another ticket: (y/n) \n")
    while user_input != "-":
        # Creating a temp list to store each ticket and user data in. This will update the nested list each time
        # option 1 is selected.
        temp_list = []
        number += 1
        #user = UserDetails()
        temp_list.append(UserDetails)

        # Ticket status
        temp_list.append("open")
        # Ticket feedback/response
        temp_list.append("Not Yet Provided")


def respond_to_a_ticket():
    print('Code to close a ticket and to give a response.')


def ticket_stats():
    print('Code to show all open, closed tickets and how many tickets to be done.')


def reopen_ticket():
    print('Code to open a closed ticket')


# Changing the menu selection to a dic.
available_selections = {
    0: "Exit Program",
    1: "Submit helpdesk ticket",
    2: "Show all tickets",
    3: "Respond to ticket by number",
    4: "Ticket stats",
    5: "Re-open resolved ticket",
}

if __name__ == '__main__':
    while True:
        print_menu()
        # User get a chance to make a selection based on the above options. Error handling.
        choice = ''
        # Handling the error if the user does not enter an integer
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number, 0 - 5')
        # Check what choice was entered and act accordingly
        if choice == 1:
            submit_helpdesk_ticket()
        elif choice == 2:
            UserDetails.show_all_tickets()
        elif choice == 3:
            respond_to_a_ticket()
        elif choice == 4:
            ticket_stats()
        elif choice == 5:
            reopen_ticket()
        elif choice == 0:
            exit_program()
        else:
            # Handling the error if the user does not enter a number in the selection range
            print('Invalid option. Please enter a number between 0 and 5.')