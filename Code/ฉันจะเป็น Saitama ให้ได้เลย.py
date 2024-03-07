"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math

#howmany
_VD = int(input())
_SD = int(input())
_LD = int(input())
_RD = int(input())
#per day
_V = int(input())
_S = int(input())
_R = int(input())
_L = int(input())

if math.ceil(_VD/_V) > math.ceil(_SD/_S) and\
    math.ceil(_VD/_V) > math.ceil(_LD/_L) and math.ceil(_VD/_V) > math.ceil(_RD/_R):
    print(math.ceil(_VD/_V))
elif math.ceil(_SD/_S) > math.ceil(_LD/_L) and math.ceil(_SD/_S) > math.ceil(_RD/_R):
    print(math.ceil(_SD/_S))
elif math.ceil(_LD/_L) > math.ceil(_RD/_R):
    print(math.ceil(_LD/_L))
else:
    print(math.ceil(_RD/_R))
