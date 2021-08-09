# Find the difference between a function defined inside a class and a function outside a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeHerOlder(self):
        self.age = self.age + 1

def makeHerOlderFromOutSide(argument: Person):
    argument.age = argument.age + 1

def makeHerOlderFromOutSideUsingInside(argument: Person):
    argument.makeHerOlder()


p1 = Person("Gholi", 12)
print(p1.age)

p1.makeHerOlder()
print(p1.age)
makeHerOlderFromOutSide(p1)
makeHerOlderFromOutSideUsingInside(p1)
print(str(p1.age))






