"""WeightStation"""

_AVG = float(input())
_X = float(input())
_Y = float(input())
_Z = float(input())

if _AVG * 4 >= 15000:
    print("Overweight")
elif abs(_AVG - _X) >= _AVG / 2 or abs(_AVG - _Y) >= _AVG / 2 or abs(_AVG - _Z) >= _AVG / 2 or\
    abs(_AVG - ((_AVG * 4) - (_X + _Y + _Z)) >= _AVG / 2):
    print("Unbalance")
else:
    print("Pass", "%.2f" % ((_AVG * 4) - (_X + _Y + _Z)))
    #if _X > _Y and _X > _Z:
    #    print("Pass", "%.2f" % _X)
    #elif _Y > _Z:
    #    print("Pass", "%.2f" % _Y)
    #else:
    #    print("Pass", "%.2f" % _Z)
