"""MissingNumber (No Set)"""

_LISTA = []
_X = int(input())
while True:
    _Y = int(input())
    if _Y == 0:
        break
    else:
        _LISTA.append(_Y)
_LISTA.sort()
for i in range(1, _X+1):
    if i not in _LISTA:
        print(i)
