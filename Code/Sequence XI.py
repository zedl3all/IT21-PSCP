"""Sequence XI"""

_IN = int(input())

for row in range(1, _IN*2):
    for col in range(1, _IN*2):
        if row > _IN:
            _X = _IN-(row-_IN)
        else:
            _X = row
        if col > _IN:
            _Y = _IN-(col-_IN)
        else:
            _Y = col
        if _X <= _Y:
            print("%02d"%_X, end=" ")
        else:
            print("%02d"%_Y, end=" ")
    print()
