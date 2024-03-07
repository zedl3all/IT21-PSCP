"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""

_AOD = input()
_X = float(input())
_Y = float(input())
_Z = float(input())

if _AOD == "Descend":
    if _X >= _Y and _X >= _Z and _Y >= _Z:
        print(str("%.2f" % _X) + ", " + str("%.2f" % _Y) + ", " + str("%.2f" % _Z))
    elif _X >= _Y and _X >= _Z and _Y <= _Z:
        print(("%.2f" % _X) + ", " + ("%.2f" % _Z) + ", " + ("%.2f" % _Y))
    elif _Y >= _X and _Y >= _Z and _X >= _Z:
        print(("%.2f" % _Y) + ", " + ("%.2f" % _X) + ", " + ("%.2f" % _Z))
    elif _Y >= _X and _Y >= _Z and _X <= _Z:
        print(("%.2f" % _Y) + ", " + ("%.2f" % _Z) + ", " + ("%.2f" % _X))
    elif _Z >= _X and _Z >= _Y and _X >= _Y:
        print(("%.2f" % _Z) + ", " + ("%.2f" % _X) + ", " + ("%.2f" % _Y))
    elif _Z >= _X and _Z >= _Y and _X <= _Y:
        print(("%.2f" % _Z) + ", " + ("%.2f" % _Y) + ", " + ("%.2f" % _X))
elif _AOD == "Ascend":
    if _X <= _Y and _X <= _Z and _Y <= _Z:
        print(str("%.2f" % _X) + ", " + str("%.2f" % _Y) + ", " + str("%.2f" % _Z))
    elif _X <= _Y and _X <= _Z and _Y >= _Z:
        print(("%.2f" % _X) + ", " + ("%.2f" % _Z) + ", " + ("%.2f" % _Y))
    elif _Y <= _X and _Y <= _Z and _X <= _Z:
        print(("%.2f" % _Y) + ", " + ("%.2f" % _X) + ", " + ("%.2f" % _Z))
    elif _Y <= _X and _Y <= _Z and _X >= _Z:
        print(("%.2f" % _Y) + ", " + ("%.2f" % _Z) + ", " + ("%.2f" % _X))
    elif _Z <= _X and _Z <= _Y and _X <= _Y:
        print(("%.2f" % _Z) + ", " + ("%.2f" % _X) + ", " + ("%.2f" % _Y))
    elif _Z <= _X and _Z <= _Y and _X >= _Y:
        print(("%.2f" % _Z) + ", " + ("%.2f" % _Y) + ", " + ("%.2f" % _X))
