# Asking the user for a number and storing it in a variable that 
# will be used later in the funtion as the argument. It has
# to be and integer number.
num = int(input(print("Can you please enter a number>")))

# Confirming back to the user the numnber they have entered.
print("Your number is ", num)

# Creating a function with an argument
def multiples(number):
    # Proving a counter for the while loop
    counter = 1
    base = number

    # While the counter is smaller than 4 (hard coded) the program will 
    # add the number the user entered to base and print it.
    # The next round it will add the user number to the existing number.
    while counter <= 4:
        number += base
        counter += 1
        print(number)

# Calling a function and providing the argument
multiples(num)
