# Creatig a simpler for loop.
# The user determines how many times the loop will executes.
# user_input = int(input("Please enter the number of times: "))
#
# For loop - with each iteration the string is printed and index is adding 1.
# for i in range(user_input):
#     print("Hello world..", i+1)

# Asking the user how many times the for loop to run
user_input = int(input("please enter a number for the size of the shape: "))

# Creating a nested loop
for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')

# Creating a nested loop, but the reverse of the above
for i in range(user_input, 0, -1):
    for j in range (i):
        print('* ', end="")
    print('')
