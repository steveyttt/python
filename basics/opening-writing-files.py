from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you do want that hit RETURN.")

input("?")

print("Opening the file...")
### FYI "w" opens the file for writing and truncates it first
### USE a to append
target = open(filename, "w")

### You dont need to do this if you specify "w" to the open function
print("Truncating the file, Goodbye!")
target.truncate()

print("Now i am going to ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(f"""
{line1}
{line2}
{line3}
""")

print("And finally, we close it")
target.close()

print("Now we re-open the file with a RO connection")
textfile = open(filename)
print(textfile.read())
textfile.close()
