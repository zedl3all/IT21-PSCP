"""Brick Bridge"""

#import time
#start = time.time()

_A = int(input())
_B = int(input())
_G = int(input())
_COUNT = 1

for i in range(_B):
    
    if _COUNT * 5 > _G:
        break
    _COUNT += 1

_COUNT = (_COUNT-1) * 5
_COUNT2 = 0

for i in range(_A):
    if _COUNT == _G:
        break
    _COUNT += 1
    _COUNT2 += 1

if _COUNT < _G:
    print("-1")
else:
    print(_COUNT2)

#end = time.time()
#print("The time of execution of above program is :",(end-start) * 10**3, "ms")
#print("The time of execution of above program is :",(end-start), "s")
