"""RockPaperScissor"""

_X = str(input())

_CA = 0
_CB = 0

for i in range(0, len(_X), 2):
    #print(_X[i:i+2])
    _Y = _X[i:i+2]
    if _Y[0] == "R" and _Y[1] == "P":
        _CB += 1
    elif _Y[0] == "R" and _Y[1] == "S":
        _CA += 1
    elif _Y[0] == "P" and _Y[1] == "R":
        _CA += 1
    elif _Y[0] == "P" and _Y[1] == "S":
        _CB += 1
    elif _Y[0] == "S" and _Y[1] == "P":
        _CA += 1
    elif _Y[0] == "S" and _Y[1] == "R":
        _CB += 1

if _CA > _CB:
    print("A win", str(_CA)+"-"+str(_CB))
elif _CB > _CA:
    print("B win", str(_CB)+"-"+str(_CA))
else:
    print("DRAW", _CA)
