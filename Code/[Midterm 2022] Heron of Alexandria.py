"""[Midterm 2022] Heron of Alexandria"""

import math

_A = float(input())
_B = float(input())
_C = float(input())
_S = (_A+_B+_C)/2
_AREA = math.sqrt(_S*(_S-_A)*(_S-_B)*(_S-_C))

print("%.3f" % _AREA)
