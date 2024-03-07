"""[Midterm 2022] Palindrome"""

_N = int(input())
_T = str(input())

_H = ""
_M = ""
_COUNT = 0

for i in _T:
    if str(i) == ":":
        _COUNT += 1
        continue
    if _COUNT > 0:
        _M += i
    else:
        _H += i

_H = int(_H)
_M = int(_M)

for i in range(1,_N+1):
    _M += 10
    print(str(_H) + ":" + str(_M))

#print(_H, _M)