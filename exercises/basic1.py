from sys import version
from datetime import datetime
from math import pi
import re

print("""
Twinkle
    How i wonder
        up above
        like a diamon
twinkle twinkle
    how i wonder
""")

print(version)

timenow = datetime.now(tz=None)
print(timenow)

print("The area of a circle with a radius of 1.24 is...", (pi * 1.24**2))


userstuff = input("Give me 5 numbers: ")

userstufflist = userstuff.split(" ")
userstufftuple = tuple(map(int, userstuff.split(' ')))

print(userstufflist)
print(userstufftuple)

# filename = input("give me a file name")
filename = "bobb.json.frog.bob.bib"

# fileextension = filename.split(".")
# print(fileextension[1])

fileextension = filename.split(".")
print(fileextension[-1])
# print(fileextension)

print(str.rsplit(filename, sep=None, maxsplit=-1))

print(timenow.__doc__)