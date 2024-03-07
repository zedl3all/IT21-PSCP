"""Median"""

_N = int(input())
_L = []

for i in range(_N):
    _X = int(input())
    _L.append(_X)
_L.sort()
if _N % 2 != 0:
    print("%.1f" % (_L[_N // 2]))
else:
    print("%.1f" % ((_L[_N // 2] + _L[(_N // 2) - 1]) / 2))
