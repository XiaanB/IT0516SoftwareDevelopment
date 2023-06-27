class Person:
    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address
        self.height = height

    def display(self):
        print("age: ", self.age)
        print("gender: ", self.gender)
        print("address: ", self.address)
        print("height: ", self.height)


harry = Person(30, "Male", "califarnia", 1.79)
harry.display()
