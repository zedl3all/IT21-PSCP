"""Blackjack"""

_X = int(input())
_CAL = 0
_C1 =""
_C2 =""
_C3 =""

if _X == 2:
    _C1 = str(input())
    _C2 = str(input())
elif _X == 3:
    _C1 = str(input())
    _C2 = str(input())
    _C3 = str(input())

if _C1.isidentifier() == True and _C1 != "A" or _C2.isidentifier() == True and _C2 != "A" or _C3.isidentifier() == True and _C3 != "A":
    _CAL += 10
elif _C1 == "A" or _C2 == "A" or _C3 == "A":
    if _CAL + 11 > 21:
        _CAL += 1
    else:
        _CAL += 11
else:
    _CAL += int(_C1)
    _CAL += int(_C2)
    _CAL += int(_C3)

if _C2 == "A" and _CAL > 21:
    _CAL -= 10

print(_CAL)