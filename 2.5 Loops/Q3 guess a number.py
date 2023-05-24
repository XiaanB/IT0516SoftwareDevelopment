import random

number = random.randint(1, 10)
number_of_tries = 5

while True:
    print("Guess a number between 1 and 9!!")
    print("You have ", number_of_tries, " opportunities. ")
    user_input = int(input("Please enter a number between 0 and 10: "))

    if user_input < 0 or user_input > 10:
        print("Please try a different number!")
    if user_input != number:
        number_of_tries -= 1
        print("You have ", number_of_tries, " left. \n Tr again.")
        if number_of_tries == 0:
            print("You are out of tries, better luck next time...")
            break
    if user_input == number:
        print("Well done")
        break

