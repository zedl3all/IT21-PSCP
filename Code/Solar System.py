"""Solar System"""

_X = str(input())
_Y = ""

for i in _X:
    if i != " ":
        _Y += i
    if i.isupper():
        print(i)
print(_Y)
print(_Y.index("Sun"))
print(len(_Y))