"""arrow"""

_A = int(input())
_B = int(input())
_C = _B // 2

for i in range(_C):
    print(" " * (_C - (i + 1)), "*" * _A)

print("*" * _A)

for i in range(_C):
    print(" " * i, "*" * _A)
