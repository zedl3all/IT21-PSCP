"""SaveComputeRepeat"""

_MIL = 492137954293754252786
_SEC = _MIL // 1000
_MIL = _MIL % 1000
_MIN = _SEC // 60
_SEC = _SEC % 60
_H = _MIN // 60
_MIN = _MIN % 60
_D = _H // 24
_H = _H % 24

print(_D, _H, _MIN, _SEC, _MIL)
