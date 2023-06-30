# Creating a funtion with a argument that takes that argument and
# adds 1 to it and then prints it.
def get_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is {0}.\n"
          .format(param_score))
    return param_score

# Variable with the initial score value
score = 4
# Printing the initial score value and a message
x = input("Your score is {0} points...\n\n"
          " Hit any key to get another point. "
          .format(score))

# Calling the funtion 
score = get_new_score(score)
