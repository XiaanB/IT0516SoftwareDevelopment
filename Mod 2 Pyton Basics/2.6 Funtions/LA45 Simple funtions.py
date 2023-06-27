# # 1
# def welcome():
#     """Welcome message then the result of adding 2 integers"""
#     print("Welcome to the program.")
#
#
# def add_numbers(x, y):
#     print(x + y)
#
#
# welcome()
#
# number_one = int(input(print("Please enter the first number: ")))
# number_two = int(input(print("Please enter the second number")))
#
# add_numbers(number_one, number_two)

# #2
#"""Print the entered word the amount of times the user specifies"""
# x = int(input(print("Please enter the number of times you would like to repeat: ")))
# y = input(print("Please enter the word you would like to repeat."))
#
# def display_multiple(x, y):
#     print((y,) * x)
#
#
# display_multiple(x, y)

#3
import random


def random_number():
    user_input = input(print("Please type the letter r to print a random number, any other letter to exit."))
    while user_input.lower() == "r":
        user_input = input(print("Please type the letter r to print a random number, any other letter to exit."))
        print(random.randint(0, 1000))

    # if user_input.lower() == "r":
    #     print(random.randint(0, 1000))
    # else:
    #     exit()

random_number()