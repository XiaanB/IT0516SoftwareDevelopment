first_number = 1500
second_number = 2700


for i in range(first_number, second_number):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i, end=" ")


