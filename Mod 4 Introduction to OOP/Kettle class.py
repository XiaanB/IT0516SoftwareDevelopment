# Different use of funtions
a = 12
b = 4
print(a+ b)
print(a.__add__(b))


# Creating  Kettle class with attributes
class Kettle(object):
    
    # Class attribute
    power_source = "Electricity"
    
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
        # Adding a function to turn the kettle on.
        
    def switch_on(self):
        self.on = True

# Creating instances
kenwood = Kettle("Kenwodd", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# Data attributes of the class instances
print("Models: {0.make} = {0.price}, {0.make} = {0.make}".format(kenwood, hamilton))

# Using the on function to turn the kettle on.
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Calling the method of the class
Kettle.switch_on(kenwood)
print(kenwood.on)

# Adding a power attribute to the kenwood instance, not the hamilton
print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
