class Animal(object):

    def __init__(self, name):
        self.name = name

    def myname(self):
        print(self.name)

class Dog(Animal):

    def __init__(self, name):
        self.name = name

mydog = Animal("rover")

yourdog = Dog("bandit")


print(mydog.name)
print(mydog.myname())
# print(yourdog.name())
