"""[Recommend] Milk"""

_A = float(input())
_B = int(input())
_C = int(input())
_D = float(input())

_PRICE = 0
_BUY = 0

if _B == 0:
    while True:
        _PRICE += _A
        if _PRICE > _D:
            break
        _BUY += 1
else:
    while True:
        _PRICE += _A
        if _PRICE > _D:
            break
        _BUY += 1
        while True:
            if _BUY % _B == 0:
                _BUY += _C
            else:
                break

print(_BUY)
