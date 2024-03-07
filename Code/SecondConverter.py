"""SecondConverter"""

_SEC = int(input())
_S2M = int(input())
_M2H = int(input())
_H2D = int(input())


_MIN = _SEC // _S2M
_SEC = _SEC % _S2M
_H = _MIN // _M2H
_MIN = _MIN % _M2H
_H = _H % _H2D
print(str(_H) + ":" + str(_MIN) + ":" + str(_SEC))
