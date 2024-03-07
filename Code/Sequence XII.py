"""Sequence XII"""

_IN = int(input())

for row in range(1, _IN*2):
    for col in range(1, _IN*2):
        if row > _IN:
            _X = (_IN + 1) - (_IN - (row - _IN))
        else:
            _X = (_IN + 1) - row
        if col > _IN:
            _Y = (_IN + 1) - (_IN - (col - _IN))
        else:
            _Y = (_IN + 1) - col
        print("%02d" % (_IN - abs(_X - _Y)), end=" ")
    print()
