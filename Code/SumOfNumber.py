"""SumOfNumber"""

_Y = 0
_Z = int(input())

while True:
    if _Y == _Z:
        break
    _X = int(input())
    if _X == -1:
        break
    _Y += _X

print(_Y)
