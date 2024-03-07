"""BigFrame"""

_A = str(input()).strip()
_B = str(input()).strip()
_C = str(input()).strip()
_D = str(input()).strip()
_E = str(input()).strip()

_MAX = max(len(_A), len(_B), len(_C), len(_D), len(_E))

print("*"*int(_MAX+4))
print("*", _A + " "*(_MAX-len(_A)) + " *")
print("*", _B + " "*(_MAX-len(_B)) + " *")
print("*", _C + " "*(_MAX-len(_C)) + " *")
print("*", _D + " "*(_MAX-len(_D)) + " *")
print("*", _E + " "*(_MAX-len(_E)) + " *")
print("*"*int(_MAX+4))
