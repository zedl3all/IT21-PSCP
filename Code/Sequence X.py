"""Sequence X"""

_N = int(input())

for row in range(1, _N + 1):
    _COUNT = 1
    for col in range(1, _N * 2):
        if col > _N-row and col < _N:
            print("%02d" % _COUNT, end=" ")
            _COUNT += 1
        elif col >= _N and _COUNT > 0:
            print("%02d" % _COUNT, end=" ")
            _COUNT -= 1
        else:
            print("  ", end=" ")
    print()
for row in range(_N-1, 0, -1):
    _COUNT = 1
    for col in range(1, _N * 2):
        if col > _N-row and col < _N:
            print("%02d" % _COUNT, end=" ")
            _COUNT += 1
        elif col >= _N and _COUNT > 0:
            print("%02d" % _COUNT, end=" ")
            _COUNT -= 1
        else:
            print("  ", end=" ")
    print()
