"""Align"""

_SIZE = int(input())
_POS = str(input())
_WORD = str(input())

if _POS == "left":
    print(_WORD.ljust(_SIZE))
elif _POS == "right":
    print(_WORD.rjust(_SIZE))
elif _POS == "center":
    if _SIZE-(len(_WORD))%2 != 0:
        _L = " "*(_SIZE-len(_WORD)-((_SIZE-len(_WORD))//2))
        _R = " "*((_SIZE-len(_WORD))//2)
        print(_L+_WORD+_R)
    else:
        print(_WORD.center(_SIZE))
