"""[Midterm 2022] Coke"""

_A = int(input())
_B = int(input())
_C = int(input())
_D = int(input())

_BUY = 0
_PRICE = 0
_REDUCE = 0
_COUNT = 0

if _B == 0:
    print(_A*_D)
else:
    while _BUY < _D:
        if _COUNT == _B:
            _REDUCE += 1
            _COUNT = 0
        _COUNT += 1
        _BUY += 1
    print(((_BUY*_A)-(_REDUCE*_A))+(_REDUCE*_C))
