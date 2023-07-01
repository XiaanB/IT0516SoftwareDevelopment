# Creating a class person with 4 properties
class Person:
    # INitializing 
    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address
        self.height = height

    # Fuction to display
    def display(self):
        print("age: ", self.age)
        print("gender: ", self.gender)
        print("address: ", self.address)
        print("height: ", self.height)


# Creating harry
harry = Person(30, "Male", "califarnia", 1.79)
# Useing the display function
harry.display()
