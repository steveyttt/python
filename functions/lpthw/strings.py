# simple
def print_two(*args):
    arg1, arg2, = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Pointless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# more pointless
def print_one(arg1):
    print(f"arg1: {arg1}")

#This takes no args
def print_none():
    print("I got nothing")


print_two("Steve","Tyson")
print_two_again("Steve","Tyson")
print_one("First")
print_none()

b = open("file")
b.seek
