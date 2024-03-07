"""[Midterm 2022] Calculator"""

_N = int(input())
_NUM = ""

if _N == 1:
    print(_N)
else:
    for i in range(1, _N+1):
        _NUM += str(i)+"+"
    print(len(_NUM))
