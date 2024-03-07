"""[Midterm 2022] Meteorite"""

_A = float(input())
_B = int(input())
_C = float(input())
_COUNT = 0
_CAL = _A
_NUB = 0

if _A < _C:
    print(0)
elif _A / _B < _C:
    print(1)
else:
    while True:
        if _CAL < _C:
            break
        else:
            _CAL = _CAL / _B
            _COUNT += 1
    for i in range(_COUNT):
        _NUB += _B**i
    print(_NUB)
