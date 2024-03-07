"""K_Aprek_Ars"""

_X = int(input())
_DEPO = 0
_A = 0
_B = 0
_C = 0
_D = 0
_COUNT = 0

while True:
    _A = int(_X/1000)
    _X = _X-(_A*1000)
    _B = int(_X/100)
    _X = _X-(_B*100)
    _C = int(_X/10)
    _X = _X-(_C*10)
    _D = _X

    while True:
        if _B < _A:
            _DEPO = _A
            _A = _B
            _B = _DEPO
        elif _C < _B:
            _DEPO = _B
            _B = _C
            _C = _DEPO
        elif _D < _C:
            _DEPO = _C
            _C = _D
            _D = _DEPO
        else:
            break

    _LOW = str(_A)+str(_B)+str(_C)+str(_D)
    _HIGH = str(_D)+str(_C)+str(_B)+str(_A)
    _X = int(_HIGH) - int(_LOW)
    _COUNT += 1
    if _X == 6174:
        break

#print(_A)
#print(_B)
#print(_C)
#print(_D)
#print(_LOW)
#print(_HIGH)
#print(_X)
print(_COUNT)
