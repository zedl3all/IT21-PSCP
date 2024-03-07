"""Timing II"""

_SEC = int(input())
_MIN = _SEC // 60
_SEC = _SEC % 60
_H = _MIN // 60
_MIN = _MIN % 60
_D = _H // 24
_H = _H % 24

if _D > 9999:
    print("ERR_:__:__:__")
else:
    print("%04d"%_D + ":" + "%02d"%_H + ":" + "%02d"%_MIN + ":" + "%02d"%_SEC)
