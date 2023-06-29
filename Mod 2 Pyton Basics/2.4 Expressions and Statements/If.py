# Parking meter calculation
# Print a greeting
print("Kia Ora, this is a parking meter.")

# Variable to store the user input and then pritning the user input back to him.
park_time = int(input("How long did you park for?"))
print("park_time time is ", park_time, "hours.")

# Creating variables.
rate = 4
cost = 0

# Doing the calculations. If parked for more than 3 hours on calculation and if 
# parked for less than 3 hours there is another calculation.
if park_time > 3:
    cost = rate*3
    rate -= 2
    park_time -= 3
    cost += rate*park_time
    print("The total cost of the parking is: $", cost)
else:
    cost = park_time * rate
    print("The cost of parking is $:", cost)
