"""Bill"""

_X = int(input())
_BILL = _X
_CAL1 = _X*(10/100)

if _CAL1 < 50:
    _BILL += 50
elif _CAL1 > 1000:
    _BILL += 1000
else:
    _BILL += _CAL1

_BILL += _BILL*(7/100)

print("%.2f" % _BILL)
