##

print(2 + 3 * 6)
print((2 + 3) * 6)
print(48565878 * 578453)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print(2+2)
print((5 - 1) * ((7 + 1) / (3 - 1)))

#int is a full number (No decimals)
#float can contain decimals

print(str('0'))
print(int(55.34))
print(float(99.8765))

bobage = 55

print("bob is", bobage, "years old")
### f before the string indicates that it needs to be formatted
print(f"bob is {bobage} years old")

types_of_people = 10
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y =f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"if i said: {x}")
print(f"I also said: {y}")

Hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(Hilarious))

w = "This is the left side of..."
e = "A string with a right side"

print(w + e)

print(
    """
    Hello there how are you today?
    Hello there how are you today?
    """
)

print("I\nLike\nPotatoes\nDo you..... \t like potatoes?")

print("I am 6'2\" tall")