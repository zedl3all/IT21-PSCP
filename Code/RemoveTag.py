"""RemoveTag"""

_X = str(input())
_PREOUT = ""
_CHECK = False

for i in _X:
    if i == "<":
        _CHECK = True
        _PREOUT += " "
    if i == ">":
        _CHECK = False
    elif i != "" and _CHECK is False:
        _PREOUT += i
print(_PREOUT.split())
