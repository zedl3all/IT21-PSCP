"""[Recommend] RuleofThree"""

_NUM = int(input())
_CAL = 0
_OUTPUT = ""
_CHECKM = 0
_CHECKG = 0

for i in range(_NUM):
    _MONEY = float(input())
    _GRAM = float(input())
    if _GRAM/_MONEY == _CAL:
        if _CHECKM > _MONEY:
            _OUTPUT = "%.2f %.2f" % (_MONEY, _GRAM)
        else:
            _OUTPUT = "%.2f %.2f" % (_CHECKM, _CHECKG)
    elif _GRAM/_MONEY > _CAL:
        _CHECKM = _MONEY
        _CHECKG = _GRAM
        _CAL = _GRAM/_MONEY
        _OUTPUT = "%.2f %.2f" % (_MONEY, _GRAM)

print(_OUTPUT)
