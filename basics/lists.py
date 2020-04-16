from random import randint

ten_things = "Apples Oranges Crows telephone Light Sugar"

print("My list contains", ten_things)

print("Wait, there are not ten things in that list, lets fix it!")

### split will take a string, then convert it to a list.
### the split function takes a seperator to know what to split the string on
stuff = ten_things.split(' ')
print("my list after a split....")
print(stuff)

more_stuff = ["Girl", "Boy", "Dog", "Cat", "Sausage", "Pasta", "Flames",]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding...", next_one, "...To the list")
#     stuff.append(next_one)
#     print(f"There are  {len(stuff)} items now")

for s in more_stuff:
    if len(stuff) >= 10:
        break
    else:
        print("Adding...", s, "...To the list")
        stuff.append(s)


print("There we go: ", stuff)

print(stuff[0])
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

for i in range (len(stuff)):
    print(stuff[i])

for i in stuff:
    print(i)

picker = (randint(0, (len(stuff))))

if not picker == 0:
    picker -= 1

print("random integer selected is...", picker)
print("length of list is...", len(stuff))
# print(picker)
print(stuff[picker])