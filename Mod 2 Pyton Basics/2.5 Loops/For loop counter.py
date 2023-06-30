import time

#For loop counting up from 1 to 10
for i in range(10):
    print(i+1)

# For loop counting from 50 to 100 in increments of 2.
for i in range(50,100+1,2):
    print(i)

# For loop iterating over a string and printing each caracter
for i in "christiaan":
    print(i)

# For loop counting down from 10 to 1 in increments of 1
for seconds in range(10,0,-1):
    print(seconds)
    # Putting a dealy on the counter.
    time.sleep(1)
print("happy new year")
