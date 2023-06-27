#Returning data

number = int(input(print("Can you please enter a number>")))

times = int(input(print("How many times")))


print("Your number is " , number)


def multiples(number, times):
    counter = 1

    base = number

    while counter <= times:

        number += base

        counter += 1

        print(number)


multiples(number, times)


