"""Impostor"""

_DICTX = {}
_LISTX = []
_LISTROLE = []
_LISTDIE = []
_ROLEDIE = []
while True:
    _X = str(input())
    if _X == "Start":
        break
    else:
        _X = _X[1:-1:]
        _X = _X.split(":")
        _X[0] = _X[0][1:-2:]
        _X[1] = _X[1][2:-1:]
        _DICTX[_X[0]] = _X[1]
        _LISTX.append(_X[0])
        _LISTROLE.append(_X[1])
while True:
    _X = str(input())
    if _X == "End":
        break
    else:
        _LISTDIE.append(_X)

_LISTDIE.sort()
for i in _LISTDIE:
    _ROLEDIE.append(_DICTX[i])
_ALIVE = [x for x in _LISTX if x not in _LISTDIE]
_ALIVE.sort()
_DIE = _LISTDIE

_DIMPOS = _ROLEDIE.count("Impostor")
_AIMPOS = _LISTROLE.count("Impostor")

print((_AIMPOS-_DIMPOS), "Impostor Remains")
print("***Alive***")
for i in _ALIVE:
    print(i, ":", _DICTX[i])
print("***Dead***")
for i in _DIE:
    print(i, ":", _DICTX[i])
