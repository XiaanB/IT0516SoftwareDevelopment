# Calculating the area of volume of a retangle. The user provide the mesuarements and they are stored in
# variables. 
hight = int(input("What is the hight of your cuboid? "))
lenght = int(input("What is the lenght of your cuboid? "))
width = int(input("What is the width of your cuboid? "))

# Varaible to store the user selection
selection = int(input("Please selct #1 if you would like to know the surface area or #2 if you would like to know the volume:"))

# If statement to tell the program what to do from the user selection.
if selection == 1:
    print("The surface area is:", (2*lenght*width) + (2*lenght*hight) + (2*hight*width))

elif selection == 2:
    print("The volume is:", lenght * hight * width)
else:
    print('Please make a valid selection.')
