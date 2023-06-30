#Returning data

# Creating a funtion with 2 arguments
def multiples(number, times):
    # Creating 2 variables, one for a counter and one for 
    # start number
    counter = 1
    base = number

    # A while loop using the funtion arguments to loop
    # and add number. Also a counter counting up.
    while counter <= times:
        number += base
        counter += 1
        print(number)

# Creating 2 variabes to store user input.
user_number = int(input("Can you please enter a number: "))
user_times = int(input("How many times: "))

# Calling a funtion and using the 2 variables fom the user input as
# arguments
multiples(user_number, user_times)

