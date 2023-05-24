#4
#import math

def cm(feet = 0, inches = 0):
    """Converting feet and inches to cm"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

print(cm(feet = 5))
print(cm(inches = 70))
print(cm(5, 8))






#3
# import math
# def triangle_area(b, h):
#     """Return the area of a triangle with base b and height h."""
#     return 0.5 * b * h
# print(triangle_area(3, 6))


# 2
# import math
# print(dir(math))
# print(math.pi)
#
# def volume(r):
#     """Return the volume of a sphere with radius r"""
#     v = (4.0/3.0) * math.pi * r**3
#     return v
# print(volume(2))


#1
# def show_hello():
#     print("Hello there, this is my first function...\n\n")
#
# show_hello()
# show_hello()