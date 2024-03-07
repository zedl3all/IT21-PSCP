"""kayak"""

_N = int(input()) - 1
_P = input()

_LM1 = []
_CAL = 0

_L = _P.split()

for i in range(len(_L)):
    _L[i] = int(_L[i])

_L.sort()


for i in range(_N):
    for i in range(len(_L) - 1):
        _LM1.append(_L[i + 1] - _L[i])
    # print("LM1",_LM1)
    _POSITION_MIN = _LM1.index(min(_LM1))
    # print("minnumber",min(_LM1))
    # print("minindex",_POSITION_MIN)
    _CAL += _LM1[_POSITION_MIN]
    # print("cal",_CAL)
    _LM1 = []
    del _L[_POSITION_MIN]
    del _L[_POSITION_MIN]


# print(_LM1)
print(_CAL)
# print(_L)
