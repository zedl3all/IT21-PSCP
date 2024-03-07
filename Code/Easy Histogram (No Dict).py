"""Easy Histogram (No Dict)"""

_STR = str(input())
_LETTERCOUNT = []

for i in _STR:
    if i.isalpha():
        _LETTERCOUNT.append(i)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    _LOWER_COUNT = _LETTERCOUNT.count(letter)
    _UPPER = letter.upper()
    _UPPER_COUNT = _LETTERCOUNT.count(_UPPER)
    if _LOWER_COUNT > 0:
        print(letter, "=", _LOWER_COUNT)
    if _UPPER_COUNT > 0:
        print(_UPPER, "=", _UPPER_COUNT)
