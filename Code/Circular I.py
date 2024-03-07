"""Point in Circle"""
import math

def circle():
    """hello"""
    xebra = float(input())
    yeed = float(input())
    russamee = float(input())
    xnpoint = float(input())
    ynpoint = float(input())
    cal = math.sqrt((xnpoint-xebra)**2 + (ynpoint-yeed)**2)
    if cal <= russamee:
        print("Yes")
    else:
        print("No")

circle()
