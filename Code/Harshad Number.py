"""Harshad Number"""

for i in range(10):
    _X = abs(int(input()))
    _X = str(_X)
    if len(_X) == 1:
        if _X == "0":
            print("No")
        else:
            print("Yes")
    else:
        _Y = []
        _Z = 0
        for i in _X:
            _Y.append(int(i))
        _Z = sum(_Y)
        if int(_X) % _Z == 0:
            print("Yes")
        else:
            print("No")
