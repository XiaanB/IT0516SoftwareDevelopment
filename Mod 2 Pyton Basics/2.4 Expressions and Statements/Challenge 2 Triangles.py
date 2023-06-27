side_a = int(input("Please enter the length of side a: "))
side_b = int(input("Please enter the length of side b: "))
side_c = int(input("Please enter the length of sode c: "))

if side_a == side_b & side_b == side_c & side_a == side_c:
    print("This triangle is a scalene triangle")

# elif side_a == side_b & side_a != side_c\
#     or side_a == side_c & side_a != side_b\
#     or side_b == side_c & side_b != side_a:
#   print("This triangle is a isoceles triangle.")

if side_a == side_b and side_a != side_c \
        or side_a == side_c and side_a != side_b \
        or side_b == side_c and side_b!= side_a:
    print("The triangle is isoceles")

else:
    print("This triangle is a scalar triangle.")


