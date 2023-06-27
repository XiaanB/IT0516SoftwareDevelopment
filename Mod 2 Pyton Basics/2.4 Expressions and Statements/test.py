side_a = int(input("Enter the length of the first side\n\n"))
side_b = int(input("Enter the width of the second side\n\n"))
side_c = int(input("Enter the height of the third side\n\n"))
if side_a == side_b == side_c:
    print("The triangle is equilateral")
if side_a == side_b and side_a != side_c \
        or side_a == side_c and side_a != side_b \
        or side_b == side_c and side_b!= side_a:
    print("The triangle is isoceles")
if side_a != side_b != side_c :
    print("The triangle is scalar")
# Testing
'''
print("My assertions are:"
"\nside_a = 6, side_b = 6, side_c = 6, output = equilateral"
"\nside_a = 6, side_b = 5, side_c = 5, output = isoceles"
"\nside_a = 5, side_b = 6, side_c = 5, output = isoceles"
"\nside_a = 5, side_b = 5, side_c = 6, output = isoceles"
"\nside_a = 6, side_b = 5, side_c = 4, output = scalar")
'''
