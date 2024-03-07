"""GraderMachine"""

_X = int(input())
_Y = int(input())
_P1 = "pass :"
_P2 = 0

if _X < _Y:
    for _ in range(_X, _Y + 1):
        if _ % 2 == 0:
            _P1 = _P1 + " " + str(_)
            _P2 += _
else:
    for _ in range(_X, _Y - 1, -1):
        if _ % 2 == 0:
            _P1 = _P1 + " " + str(_)
            _P2 += _

print(_P1)
print("Sum :", _P2)
