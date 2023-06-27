class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def my_intro(self):
        print("Hello my gender is " + self.gender)
        print('Hello my age is ', self.age)


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