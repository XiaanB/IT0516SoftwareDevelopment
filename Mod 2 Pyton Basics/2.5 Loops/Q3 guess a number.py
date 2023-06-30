import random

# Creating a variable to store a random number between 1 and 10
number = random.randint(1, 10)
# Creating a variable for the number of tries allowed.
number_of_tries = 5

while True:
    print("Guess a number between 1 and 9!!")
    print("You have ", number_of_tries, " opportunities. ")
    user_input = int(input("Please enter a number between 0 and 10: "))

    # Comaring the user input to the randome number.
    if user_input < 0 or user_input > 10:
        print("Please try a different number!")
    # If the user input is not equal to the random number, reduce the number of tries.    
    if user_input != number:
        number_of_tries -= 1
        print("You have ", number_of_tries, " left. \n Tr again.")
        # Defiuning what happens when the user tries are finished
        if number_of_tries == 0:
            print("You are out of tries, better luck next time...")
            break
    # Printing a message and defining what happens if the user quess the right nuber.        
    if user_input == number:
        print("Well done")
        break

