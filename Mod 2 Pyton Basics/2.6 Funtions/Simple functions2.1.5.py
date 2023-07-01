# Functions with 2 arguments and returning a result
def multiply(x, y):
    result = x * y
    return result

# Creating a variable to store the returned value of the function
answer = multiply(10.5, 4)
print(answer)

# Creating a loop
for val in range(1, 5):
    # Creating a variable to store result  from calling the method
    two_times = multiply(2, val)
    print(two_times)
