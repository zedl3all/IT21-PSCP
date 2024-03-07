"""[Midterm 2022] Volleyball"""

_X = str(input())
_A = 0
_B = 0

for i in _X:
    if _A > _B+2 and _A > 25:
        print("AWIN",_A)
        _A = 0
        _B = 0
    elif _B > _A+2 and _B > 25:
        print("BWIN",_B)
        _A = 0
        _B = 0
    if i == "A":
        _A += 1
    elif i == "B":
        _B += 1

