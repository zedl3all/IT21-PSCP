"""[Midterm 2021] B - Fully pair?"""

_X = str(input())
_OUT = ""

for i in _X:
    if i in _OUT:
        pass
    else:
        if _X.count(i) % 2 != 0:
            _OUT += i

if _OUT == "":
    print("fully paired")
else:
    print(_OUT)
