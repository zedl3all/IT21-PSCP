"""Turnstile"""

_DATA = ""
_COUNT = 0

while True:
    _X = str(input())
    if _X == "END":
        break
    _DATA += _X

for i in range(1, len(_DATA)):
    if _DATA[i] == "P" and _DATA[i-1] == "C":
        _COUNT += 1

print(_COUNT)
