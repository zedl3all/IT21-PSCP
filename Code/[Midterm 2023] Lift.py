"""[Midterm 2023] Lift"""

_PEOPLE = int(input())
_MAXWEIGHT = float(input())
_ADULT = False
_KID = False
_ALLWEIGHT = 0

for i in range(_PEOPLE):
    _AGE = int(input())
    _WEIGHT = float(input())
    if _AGE < 12:
        _KID = True
    else:
        _ADULT = True
    _ALLWEIGHT += _WEIGHT

if _ALLWEIGHT > _MAXWEIGHT:
    print("Not Safe")
elif _KID is True and _ADULT is False:
    print("Not Safe")
else:
    print("Safe")
