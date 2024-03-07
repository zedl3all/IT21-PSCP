"""Grade II"""

_X = int(input())

_COUNT = 0

for i in range(_X):
    _GRADE = float(input())
    if _GRADE >= 95 and _GRADE <= 100:
        #print("A")
        _COUNT += 4
    elif _GRADE >= 90 and _GRADE <= 95:
        #print("B+")
        _COUNT += 3.5
    elif _GRADE >= 85 and _GRADE <= 90:
        #print("B")
        _COUNT += 3
    elif _GRADE >= 80 and _GRADE <= 85:
        #print("C+")
        _COUNT += 2.5
    elif _GRADE >= 75 and _GRADE <= 80:
        #print("C")
        _COUNT += 2
    elif _GRADE >= 70 and _GRADE <= 75:
        #print("D+")
        _COUNT += 1.5
    elif _GRADE >= 65 and _GRADE <= 70:
        #print("D")
        _COUNT += 1
    elif _GRADE >= 60 and _GRADE <= 65:
        #print("F+")
        _COUNT += 0.5
    elif _GRADE >= 0 and _GRADE <= 60:
        #print("F")
        _COUNT += 0

print("%.2f" % (int((_COUNT/_X) * 100) / 100))
