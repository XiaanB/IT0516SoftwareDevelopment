print("IT5014 Helpdesk Ticketing System:")
print("_______________________________________________________")
print("Select one of the following choices:")

Dict = {}
Dict[0] = "Exit"
Dict[1] = "Submit helpdesk ticket"
Dict[2] = "Show all tickets"
Dict[3] = "Respond to ticket by number"
Dict[4] = "Re-open resolved ticket"
Dict[5] = "Display ticket state"

for key, value in Dict.items():
    print(key, " : ", value)

print("______________________________________________________")
user_selection = int(input("Enter menu selection 0 - 5 : \n"))

if user_selection == 0:
    print("Thank you for using the IT help desk program.")
    exit()
