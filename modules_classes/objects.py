class Animal(object):
    pass

class Dog(Animal):
    
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
print(rover.name)

satan = Cat("Satan")
print(satan.name)

mary = Person("Mary")
print(mary.name)

mary.pet = satan
print(mary.pet)

frank = Employee("Frank", 120000)
print(frank.name)
print(frank.salary)

frank.pet = rover
print(frank.pet)

flipper = Fish()
crouse = Salmon()
harry = Halibut()