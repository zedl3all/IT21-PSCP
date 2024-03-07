"""Duplicate I"""

_NA = int(input())
_NB = int(input())
_A = set()
_B = set()

for i in range(_NA):
    _X = int(input())
    _A.add(_X)

for i in range(_NB):
    _X = int(input())
    _B.add(_X)

_AB = _B.intersection(_A)
_AB = sorted(_AB, reverse=True)
#print("----------------------------------")
if len(_AB) == 0:
    print("Nope")
else:
    for i in _AB:
        print(i)
