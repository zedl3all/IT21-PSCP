"""black jack"""

_L = []
_A = int(input())
_CAL = 0

for i in range(_A):
    _B = input()
    _L.append(_B)

if len(_L) == 2:

    if _L[0].isidentifier() == True and _L[0] != "A":
        _CAL += 10
    elif _L[0] == "A":
        _CAL += 11
    else:
        _CAL += int(_L[0])

    if _L[1].isidentifier() == True and _L[1] != "A":
        _CAL += 10
    elif _L[1] == "A":
        if _CAL + 11 > 21:
            _CAL += 1
        else:
            _CAL += 11
    else:
        _CAL += int(_L[1])

elif len(_L) == 3:
    if _L[0].isidentifier() == True and _L[0] != "A":
        _CAL += 10
    elif _L[0] == "A":
        _CAL += 11
    else:
        _CAL += int(_L[0])

    if _L[1].isidentifier() == True and _L[1] != "A":
        _CAL += 10
    elif _L[1] == "A":
        if _CAL + 11 > 21:
            _CAL += 1
        else:
            _CAL += 11
    else:
        _CAL += int(_L[1])

    if _L[2].isidentifier() == True and _L[2] != "A":
        _CAL += 10
    elif _L[2] == "A":
        if _CAL + 11 > 21:
            _CAL += 1
        else:
            _CAL += 11
    else:
        _CAL += int(_L[2])

print(_CAL)
