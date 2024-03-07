"""LineSorting"""

_N = int(input())
_LISTA = []

for i in range(_N):
    _X = str(input())
    _LISTA.append(_X)
_LISTA.sort(key=len)
for i in _LISTA:
    print(i)
