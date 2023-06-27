
score =4


def get_new_score(param_score):

    param_score += 1

    print("You got another point...\n"

          "Your score is {0}.\n"

          .format(param_score))

    return param_score


x = input("Your score is {0} points...\n\n"

          " Hit any key to get another point. "

          .format(score))

score = get_new_score(score)