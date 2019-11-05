#Check booleon condition
42 == 42

myAge = 32
print(myAge)
#print out the info (the booleon for myAge needs to be converted into a string)
print('Confirming myAge is less than 30 ' + str(myAge < 30))

#False
print(42 == 'Hello')
#False
print(42 == 41)
#True
print(2 != 3)
#True
print(42 < 100)
#False
print(42 >= 100)
#False
print(42 < 42)
#True
print(42 <= 42)
#True
print(42 == '42')
#True - but looks like it shouldnt be :)
print(42.0 == 42)

print("demonstrating truthy & falsey")
print(bool(0.00))
print(bool(0))
print(bool(''))