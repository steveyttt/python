def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("You tried to divide by 0")
    except:
        print("you entered the wrong thing")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by("I am a potato"))
