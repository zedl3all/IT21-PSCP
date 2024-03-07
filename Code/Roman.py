"""Roman"""

_ROMAN = str(input())
_RM = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

_NUM = 0
for i in range(len(_ROMAN)-1):
    _L = _RM[_ROMAN[i]]
    _R = _RM[_ROMAN[i+1]]
    if _L >= _R:
        _NUM += _L
    else:
        _NUM -= _L
_NUM += _RM[_ROMAN[len(_ROMAN)-1]]

print(_NUM)
