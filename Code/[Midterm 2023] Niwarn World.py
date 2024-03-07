"""[Midterm 2023] Niwarn World"""

import math

def functionx(number):
    """functionx"""
    return 2+((math.log2(number**2))/((2*number)*math.log2(number)))

def functiony(number, sember):
    """functiony"""
    return (math.sin(math.radians(30))+math.sqrt(2*sember))/(functionx(number)+3)

def functionz(kumber):
    """functionz"""
    return (functiony(kumber, kumber)**2)+((8456*(functionx(kumber)**4))/(24*kumber))

_N = float(input())
_S = float(input())
_K = float(input())

print("X:", str("%.1f" % functionx(_N)) + ",", "Y:", str("%.1f" % functiony(_N, _S)) + ","\
    , "Z:", str("%.1f" % functionz(_K)))
