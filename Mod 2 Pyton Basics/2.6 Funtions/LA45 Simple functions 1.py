def welcome():
    """Welcome message then the result of adding 2 integers"""
    print("Welcome to the program.")


def add_numbers(x, y):
    print(x + y)

welcome()

number_one = int(input("Please enter the first number: "))
number_two = int(input("Please enter the second number"))

add_numbers(number_one, number_two)
