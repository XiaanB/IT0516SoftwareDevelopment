# Creating class
class Person:
    # Use the __init__() function to assign values to object properties, or other operations 
    # that are necessary to do when the object is being created
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    # Creating a function
    def my_intro(self):
        print("Hello my gender is " + self.gender)
        print('Hello my age is ', self.age)

# Using the class to create instances
harry = Person(36, "Male")
Sarrah = Person(24, "Female")

print(harry.age)
print(Sarrah.gender)

harry.my_intro()
Sarrah.my_intro()

harry.age = 23

print(harry.age)

del harry.age

print(harry.age)
