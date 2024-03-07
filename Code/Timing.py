"""Timing"""

_SEC = int(input())
_MIN = _SEC // 60
_SEC = _SEC % 60
_H = _MIN // 60
_MIN = _MIN % 60
_D = _H // 24
_H = _H % 24
print(_D, _H, _MIN, _SEC)
