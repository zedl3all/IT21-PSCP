"""Key"""

_LIST = []
_SUMLIST = []
_X = str(input())

for _ in _X:
    _LIST.append(_)
    _SUMLIST.append(int(_))

_LAST3 = _LIST[-3:]
_NUM = ""

for _ in _LAST3:
    _NUM += _

_KEY = sum(_SUMLIST) + int(_NUM)*10

if _KEY < 1000:
    _KEY += 1000
    print(_KEY)
else:
    print(str(_KEY)[-4:])
