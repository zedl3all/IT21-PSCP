"""black jack"""

_A = int(input())
_CAL = 0
_COUNTA = 0

for i in range(_A):
    _B = input()
    if _B.isidentifier() == True and _B != "A":
        _CAL += 10
    elif _B == "A":
        _CAL += 11
        _COUNTA += 1
    else:
        _CAL += int(_B)

if _CAL > 21 and _COUNTA != 0:
    for i in range(_COUNTA):
        _CAL -= 10
        if _CAL <= 21:
            break

print(_CAL)
