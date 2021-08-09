# Find the class inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class Being:   # defining a class
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Human(Being):    # Defining a child class
    def __init__(self, name, age, family, gender):
        super().__init__(name, age)     # initialize properties of the parent class
        self.family = family
        self.gender = gender

    def change_gender(self):
        if self.gender == "man":
            self.gender = "woman"
        else:
            self.gender = "man"


class Tree(Being):
    def __init__(self, name, age, tribe, leaf):
        super().__init__(name, age)
        self.tribe = tribe
        self.leaf = leaf


b1 = Being("Mahdi", 26)
print(b1.name)
print(b1.age)

h1 = Human("Mahdi", 26, "Amini", "man")
print(h1.gender)
h1.change_gender()
print(h1.gender)