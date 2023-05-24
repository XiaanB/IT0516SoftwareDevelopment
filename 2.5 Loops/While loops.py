# is_running = True
#
# while is_running:
#     answer = input("What is the meaning of life?...")
#
#     if answer =="42":
#         print("Correct, well done")
#         is_running = False
#     else:
#         print("sorry, wrong answer."
#               "try again")
# x = input("Press any key to exit")

number_of_tries = 3

while True:
    answer = input("What is the meaning of life?...")
    if answer ==42:
        print("correct")
        break
    else:
        print("Sorry, try again")
        number_of_tries -= 1
        print("You have ", number_of_tries, "tries left")
    if number_of_tries == 0:
        print("You have ran out of tries")
        break
x = input("Press any key to exit")
