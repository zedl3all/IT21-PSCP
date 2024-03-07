"""[Recommend] Lotto"""

_NUM6 = str(input())
_NUMB2 = str(input())
_NUMF31 = str(input())
_NUMF32 = str(input())
_NUMB31 = str(input())
_NUMB32 = str(input())
_MYNUM = str(input())
_MONEY = 0

if _NUM6 == "000000":
    _NEAR1 = "000001"
    _NEAR2 = "999999"
elif _NUM6 == "999999":
    _NEAR1 = "000000"
    _NEAR2 = "999998"
else:
    _NEAR1 = "%06d" % (int(_NUM6)+1)
    _NEAR2 = "%06d" % (int(_NUM6)-1)

if _MYNUM == _NUM6:
    _MONEY += 6000000
elif _MYNUM == str(_NEAR1) or _MYNUM == str(_NEAR2):
    _MONEY += 100000
if _MYNUM[-2:] == _NUMB2:
    _MONEY += 2000
if _MYNUM[:3] == _NUMF31:
    _MONEY += 4000
if _MYNUM[:3] == _NUMF32:
    _MONEY += 4000
if _MYNUM[-3:] == _NUMB31:
    _MONEY += 4000
if _MYNUM[-3:] == _NUMB32:
    _MONEY += 4000

print(_MONEY)
