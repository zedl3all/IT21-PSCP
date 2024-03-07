"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""

_X = str(input())
_LETTER = ""

for i in _X:
    if i == ".":
        pass
    else:
        _LETTER += i

_LETTER = _LETTER.split()

_COUNT = 0
_PRELETTER = []
for i in _LETTER:
    if len(i) >= 2:
        _COUNT += i.count('a')
        _COUNT += i.count('e')
        _COUNT += i.count('i')
        _COUNT += i.count('o')
        _COUNT += i.count('u')
        if _COUNT >= 2:
            _PRELETTER.append(i)
            _COUNT = 0
        else:
            _COUNT = 0

_PRELETTER.sort()
if len(_PRELETTER) == 0:
    print("Nope")
else:
    for i in _PRELETTER:
        print(i)
