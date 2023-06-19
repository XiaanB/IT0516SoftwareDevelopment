num = int(input(print("Can you please enter a number>")))

print("Your number is ", num)


def multiples(number):
    counter = 1
    base = number

    while counter <= 4:
        number += base
        counter += 1
        print(number)


multiples(num)
