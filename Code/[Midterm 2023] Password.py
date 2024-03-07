"""[Midterm 2023] Password"""
import math

_X = str(input())
_LOWER = False
_UPPER = False
_NUMBER = False
_SC = False
_L = len(_X)
_R = 0

for i in _X:
    if i.islower():
        _LOWER = True
    if i.isupper():
        _UPPER = True
    if i.isdigit():
        _NUMBER = True
    if not i.islower() and not i.isupper() and not i.isdigit():
        _SC = True

if _LOWER is True:
    _R += 26
if _UPPER is True:
    _R += 26
if _NUMBER is True:
    _R += 10
if _SC is True:
    _R += 32

_E = int(math.log2(_R**_L))

print(_E)
if _E < 24:
    print("Very Weak")
elif _E >= 28 and _E <= 35:
    print("Weak")
elif _E >= 36 and _E <= 59:
    print("Reasonable")
elif _E >= 60 and _E <= 127:
    print("Strong")
else:
    print("Very Strong")
