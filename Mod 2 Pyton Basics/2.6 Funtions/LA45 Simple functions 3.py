import random


def random_number():
    user_input = input("Please type the letter r to print a random number, any other letter to exit.")
    while user_input.lower() == "r":
        user_input = input("Please type the letter r to print a random number, any other letter to exit.")
        print(random.randint(0, 1000))

    # if user_input.lower() == "r":
    #     print(random.randint(0, 1000))
    # else:
    #     exit()

random_number()
