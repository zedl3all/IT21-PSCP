"""[Recommend] ProgressiveTax"""

_MONEY = float(input())
_DISCOUNT = 0
_PAY = 0

if _MONEY > 4000000:
    _DISCOUNT = _MONEY - 4000000
    _PAY += _DISCOUNT*(35/100)
    _DISCOUNT = 4000000 - 2000000
    _PAY += _DISCOUNT*(30/100)
    _DISCOUNT = 2000000 - 1000000
    _PAY += _DISCOUNT*(25/100)
    _DISCOUNT = 1000000 - 750000
    _PAY += _DISCOUNT*(20/100)
    _DISCOUNT = 750000 - 500000
    _PAY += _DISCOUNT*(15/100)
    _DISCOUNT = 500000 - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 2000000 and _MONEY <= 4000000:
    _DISCOUNT = _MONEY - 2000000
    _PAY += _DISCOUNT*(30/100)
    _DISCOUNT = 2000000 - 1000000
    _PAY += _DISCOUNT*(25/100)
    _DISCOUNT = 1000000 - 750000
    _PAY += _DISCOUNT*(20/100)
    _DISCOUNT = 750000 - 500000
    _PAY += _DISCOUNT*(15/100)
    _DISCOUNT = 500000 - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 1000000 and _MONEY <= 2000000:
    _DISCOUNT = _MONEY - 1000000
    _PAY += _DISCOUNT*(25/100)
    _DISCOUNT = 1000000 - 750000
    _PAY += _DISCOUNT*(20/100)
    _DISCOUNT = 750000 - 500000
    _PAY += _DISCOUNT*(15/100)
    _DISCOUNT = 500000 - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 750000 and _MONEY <= 1000000:
    _DISCOUNT = _MONEY - 750000
    _PAY += _DISCOUNT*(20/100)
    _DISCOUNT = 750000 - 500000
    _PAY += _DISCOUNT*(15/100)
    _DISCOUNT = 500000 - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 500000 and _MONEY <= 750000:
    _DISCOUNT = _MONEY - 500000
    _PAY += _DISCOUNT*(15/100)
    _DISCOUNT = 500000 - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 300000 and _MONEY <= 500000:
    _DISCOUNT = _MONEY - 300000
    _PAY += _DISCOUNT*(10/100)
    _DISCOUNT = 300000 - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
elif _MONEY > 150000 and _MONEY <= 300000:
    _DISCOUNT = _MONEY - 150000
    _PAY += _DISCOUNT*(5/100)
    print(int(_PAY))
else:
    print(int(_PAY))
