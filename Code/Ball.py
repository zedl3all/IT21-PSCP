"""Ball"""

_X = float(input())
_X = _X*100
_COUNT = 0

while True:
    _X = _X*(3/5)
    if _X < 1:
        break
    _COUNT += 1

print(_COUNT)
