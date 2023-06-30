# Creating a loop. Ginving it a start and en value.
for i in range(0,7):
    # If the given condition is met do a spisific action. 
    if i % 3 != 0:
        print(i)
# Creating a loop and telling it the end.
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x, end=' ')
print("\n")
