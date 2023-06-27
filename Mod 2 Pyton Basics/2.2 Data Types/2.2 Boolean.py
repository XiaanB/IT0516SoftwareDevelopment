import random

this_bool = 1 > 2
print(this_bool)


male = False
male = bool(random.randint(0, 1))

if male:
    print("We will use name Rangi")
else:
    print("We will use name Anihera")

print("Test 1 ", bool(True))
print("Test 2 ", bool(False))
print("Test 3 ", bool("text"))
print("Test 4 ", bool(""))
print("Test 5 ", bool(" "))
print("Test 6 ", bool(0))
print("Test 7 ", bool())
print("Test 8 ", bool(3))
print("Test 9 ", bool(None))
