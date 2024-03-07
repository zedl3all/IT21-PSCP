"""[Midterm 2022] Parity"""

_NUM = str(input())
_EO = str(input())
_COUNT = 0

for i in _NUM:
    if i == "1":
        _COUNT += 1
if _EO == "Even":
    if _COUNT == 0 or _COUNT % 2 == 0:
        print(_NUM + "0")
    else:
        print(_NUM + "1")
else:
    if _COUNT == 0:
        print(_NUM + "1")
    elif _COUNT % 2 != 0:
        print(_NUM + "0")
    else:
        print(_NUM + "1")
