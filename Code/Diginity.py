"""Diginity"""

while True:
    _X = str(input())
    if _X == "0":
        break
    if len(_X) == 1:
        print(_X)
    else:
        _PX = _X
        _Y = []
        _Z = ""
        while True:
            for i in _PX:
                _Y.append(int(i))
                #print(_Y)
            _Z = str(sum(_Y))
            if len(_Z) == 1:
                _PX = _Z
                break
            else:
                _PX = _Z
                _Y = []
        print(_PX)
