"""[Midterm 2023] Bad Keyboard"""

_X = str(input())
_OUTPUT = ""

for i in _X:
    if i == "i":
        _OUTPUT += "o"
    elif i == "I":
        _OUTPUT += "O"
    elif i == "o":
        _OUTPUT += "i"
    elif i == "O":
        _OUTPUT += "I"
    else:
        _OUTPUT += i

print(_OUTPUT)
