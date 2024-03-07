"""Triangle I"""

_X = float(input())
_Y = float(input())
_Z = float(input())

if _X >= _Y and _X >= _Z:       # X High
    _PITA = (_Y**2)+(_Z**2)
    if _PITA >= (_X**2)-0.01 and _PITA <= (_X**2)+0.01:
        print("Yes")
    else:
        print("No")
elif _Y >= _Z:                  # Y High
    _PITA = (_X**2)+(_Z**2)
    if _PITA >= (_Y**2)-0.01 and _PITA <= (_Y**2)+0.01:
        print("Yes")
    else:
        print("No")
else:                           # Z High
    _PITA = (_X**2)+(_Y**2)

    if _PITA >= (_Z**2)-0.01 and _PITA <= (_Z**2)+0.01:
        print("Yes")
    else:
        print("No")
