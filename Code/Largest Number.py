"""Largest Number"""

_X = int(input())
_Y = int(input())
_Z = int(input())
_X = str(_X)
_Y = str(_Y)
_Z = str(_Z)

_XYZ = _X+_Y+_Z
_XZY = _X+_Z+_Y
_YXZ = _Y+_X+_Z
_YZX = _Y+_Z+_X
_ZXY = _Z+_X+_Y
_ZYX = _Z+_Y+_X

if int(_XYZ) >= int(_XZY) and int(_XYZ) >= int(_YXZ) and\
    int(_XYZ) >= int(_YZX) and int(_XYZ) >= int(_ZXY) and int(_XYZ) >= int(_ZYX):
    print(int(_XYZ))
elif int(_XZY) >= int(_YXZ) and int(_XZY) >= int(_YZX) and\
    int(_XZY) >= int(_ZXY) and int(_XZY) >= int(_ZYX):
    print(int(_XZY))
elif int(_YXZ) >= int(_YZX) and int(_YXZ) >= int(_ZXY) and int(_YXZ) >= int(_ZYX):
    print(int(_YXZ))
elif int(_YZX) >= int(_ZXY) and int(_YZX) >= int(_ZYX):
    print(int(_YZX))
elif int(_ZXY) >= int(_ZYX):
    print(int(_ZXY))
else:
    print(int(_ZYX))
