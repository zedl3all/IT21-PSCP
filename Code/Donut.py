"""Donut"""

import math

_PRICE = int(input())
_PIECE = int(input())
_FREE = int(input())
_WANT = int(input())
_PE = _PIECE + _FREE
_BALANCE = _WANT % _PE

if _BALANCE < _PIECE:
    _BONUS = _WANT // _PE
    _ALL = (_PE * _BONUS) + _BALANCE
    _PAY = (_PRICE * _PIECE * _BONUS) + (_BALANCE * _PRICE)
else:
    _BONUS = math.ceil(_WANT / _PE)
    _ALL = _PE * _BONUS
    _PAY = (_PRICE * _PIECE * _BONUS)

print(_PAY, _ALL)
