name = input("Please enter your name: ")
phone_num = input("Please enter you phone number: ")


def display(user_name, user_phone_num):
    print("\nHello there, my name is " + user_name + " and my number is " + user_phone_num)

def display1(user_name, user_phone_number):
    print("\nHello there, my name is {0} and my number is {1}."
          .format(user_name, user_phone_number.rstrip()))


display(name, phone_num)
display1(name, phone_num)
