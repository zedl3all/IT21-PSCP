"""Future Message"""

_X = input()

if _X.isnumeric():
    print("Number")
elif _X.isupper():
    print("Uppercase")
elif _X.islower():
    print("Lowercase")
elif _X.istitle():
    print("Title")
elif _X.isspace():
    print("Space")
else:
    print("Other")
