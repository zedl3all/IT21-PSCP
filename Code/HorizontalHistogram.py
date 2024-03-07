"""HorizontalHistogram"""

_STR = str(input())
_LETTERCOUNT = []

for i in _STR:
    if i.isalpha():
        _LETTERCOUNT.append(i)

for letter in 'abcdefghijklmnopqrstuvwxyz':
    _LOWER_COUNT = _LETTERCOUNT.count(letter)
    _LINE = ""
    if _LOWER_COUNT > 0:
        _COUNT = -1
        for i in range(1, _LOWER_COUNT+1):
            _COUNT += 1
            if _COUNT == 5:
                _LINE += "|"
                _COUNT = 0
            _LINE += "-"
        print(letter, ":", _LINE)
        _LINE = ""

for letter in 'abcdefghijklmnopqrstuvwxyz':
    _UPPER = letter.upper()
    _UPPER_COUNT = _LETTERCOUNT.count(_UPPER)
    _LINE = ""
    if _UPPER_COUNT > 0:
        _COUNT = -1
        for i in range(1, _UPPER_COUNT+1):
            _COUNT += 1
            if _COUNT == 5:
                _LINE += "|"
                _COUNT = 0
            _LINE += "-"
        print(_UPPER, ":", _LINE)
        _LINE = ""
