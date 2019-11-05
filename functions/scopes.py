spam = 42 #Global

def eggs():
    global eggs # make eggs a global variable
    eggs = 99
    spam = 44 #local variable
    potato = 22 # local variable
    print(eggs)
    print(spam)
    print(potato)

print(spam) #print global spam
eggs() # print all local variables

