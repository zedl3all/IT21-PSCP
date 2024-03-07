"""Nearer"""

_A = int(input())
_B = int(input())
_C = int(input())

_CALA = abs(_A - _C)
_CALB = abs(_B - _C)
if _CALA < _CALB:
    print("Alice", _CALA)
elif _CALA > _CALB:
    print("Bob", _CALB)
else:
    print("Sundaes", _CALB)
