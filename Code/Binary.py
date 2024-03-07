"""Binary"""

_X = int(input())
_OUTPUT = ""

if _X <= 1:
    print(_X)
else:
    while True:
        _OUTPUT += str(_X % 2)
        _X = _X//2
        if _X <= 1:
            _OUTPUT += str(_X)
            break
    print(_OUTPUT[::-1])
