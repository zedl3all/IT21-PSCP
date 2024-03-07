"""Bridge"""

import math

_A = int(input())
_B = int(input())
_G = int(input())
_C = _B

if _B * 5 > _G:
    _CAL = ((_B * 5) - _G) / 5
    _C = _B - math.ceil(_CAL)

if (_C * 5) + _A > _G:
    _CAL2 = ((_C*5) + _A) - _G
    _D = _A - _CAL2
    print(_D)
elif (_C * 5) + _A == _G:
    print(_A)
else:
    print("-1")
