# user_input = int(input("Please enter the number of times: "))
#
# for i in range(user_input):
#     print("Hello world..", i+1)


user_input = int(input("please enter a number for the size of the shape: "))

for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(user_input, 0, -1):
    for j in range (i):
        print('* ', end="")
    print('')