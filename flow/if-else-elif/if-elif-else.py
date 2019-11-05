print("enter a name")
name = input()

#If runs ONCE to check a condition and then performs an action
if name == "alice":
    print('Hi ' + str(name))
elif name == "bobby":
    print('Hi Bobby, not Hi Alice')
elif name == "jimmy":
    print('Hi jimmy, not Hi Alice')
else:
    print("I dont like you, you are not Alice")

print("if statement complete")
