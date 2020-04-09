#import the whole module
import random
#Only import one function from the module
from random import randint
#import all
import custom
from custom import Minus3, Add5

#Built in function
print(len("potato"))
print(random.randint(5, 10))
print("hello has " + str(len('hello')) + " letters in it." )

custom.Howdy("Steven")

#Func in a func
funcinafunc = Add5(Minus3(10))
print(funcinafunc)