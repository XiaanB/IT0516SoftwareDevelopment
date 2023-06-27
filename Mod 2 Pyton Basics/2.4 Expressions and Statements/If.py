print("Kia Ora, this is a parking meter.")

park_time = int(input("How long did you park for?"))
print("park_time time is ", park_time, "hours.")
rate = 4
cost = 0

if park_time > 3:
    cost = rate*3
    rate -= 2
    park_time -= 3
    cost += rate*park_time
    print("The total cost of the parking is: $", cost)
else:
    cost = park_time * rate
    print("The cost of parking is $:", cost)
