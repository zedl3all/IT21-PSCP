"""FOR!F-Ball"""

_X = str(input())
_POS = 1

for i in _X:
    if i == "A" and _POS == 1:
        _POS = 2
    elif i == "A" and _POS == 2:
        _POS = 1
    elif i == "B" and _POS == 2:
        _POS = 3
    elif i == "B" and _POS == 3:
        _POS = 2
    elif i == "C" and _POS == 3:
        _POS = 1
    elif i == "C" and _POS == 1:
        _POS = 3

print(_POS)
