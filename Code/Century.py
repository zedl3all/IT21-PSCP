"""Century"""
import math
_TIME = int(input())
_PRE = ""
_CENTURY = ""

for i in range(_TIME):
    _YEAR = str(input())
    for i in _YEAR:
        if i.isnumeric():
            _CENTURY += i
        else:
            _PRE += i
    if _PRE == "B.E. ":
        _CENTURY = int(_CENTURY)-543
    if int(_CENTURY) <= 0:
        print("ERROR")
        _PRE = ""
        _CENTURY = ""
    else:
        print(math.ceil(int(_CENTURY)/100))
        _PRE = ""
        _CENTURY = ""
