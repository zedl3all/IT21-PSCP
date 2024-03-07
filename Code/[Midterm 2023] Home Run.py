"""[Midterm 2023] Home Run"""

_X = int(input())
_Y = float(input())
_COUNT = 0

for i in range(_X):
    _Z = float(input())
    if _Y > _Z:
        _COUNT += 1
print(_COUNT)
