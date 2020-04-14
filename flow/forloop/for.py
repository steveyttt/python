print("My name is")
for i in range(5):
    print("Steve 5 times " + str(i))

total = 0 
#range is a keyword which can follow values between two numbers
for i in range(101):
    total = total + i
print(total)

total = 0 
#range is a keyword which can follow values between two numbers
for i in range(10,15):
    total = total + i
print(total)

counts = []

for x in range (2, 12):
    print(f"Adding {x} to the counts variable")
    counts.append(x)

print(counts)

for x in counts:
    print(x)

if 100 is 100:
    print("100 is 100")

if 100 in counts:
    print(f"The var {counts} contains the number 7")
elif 9 in counts:
    print(f"The var {counts} contains the number 9")
elif 55 in counts:
    print(f"The var {counts} contains the number 55")

