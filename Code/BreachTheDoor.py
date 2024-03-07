"""BreachTheDoor"""

_X = str(input())
_STR = ""
_OUT = ""

for i in _X:
    if i.isalpha() or i.isspace():
        _STR += i
_LIST = _STR.split()
for i in _LIST:
    if len(i) > 6:
        _OUT += i + " "
print(_OUT[:-1])
