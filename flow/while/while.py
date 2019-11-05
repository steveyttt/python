
#While executes multiple times until the while condition is false
spam = 0
while spam < 5:
    print("Spam is " + str(spam))
    spam = spam +1

while True:
    print("Please type your name.")
    name = input()
    if name == "your name":
        #Break will break from the loop
        break
print("Thank you!")

spams = 0
while spams < 5:
    spams = spams + 1 
    if spams == 3:
        #Continue will loop back to the beginning
        continue
    print("spams is " + str(spams))