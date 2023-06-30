# Creating 2 variables to hold the numbers
first_number = 1500
second_number = 2700

# Creating a for loop with the 2 variables as the start and end.
for i in range(first_number, second_number):
    # If both of the following conditions are met, do something (print)
    if (i % 7 == 0) and (i % 5 == 0):
        print(i, end=" ")


