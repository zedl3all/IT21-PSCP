"""Regulation"""

_A = int(input())
_B = float(input())
_C = str(input())

# print(" "*(30-_A) + str(_A))
# print("0"*(30-_A) + str(_A))
print("%30s" % _A)
print("%030d" % _A)
print("%.2f"%_B)
print("%.12f"%_B)
print("%40s" % _C)
