"""FourDirections"""

_X = str(input())
_UP = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
_DOWN = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
_LEFT = ["  *  ", " *   ", "*****", " *   ", "  *  "]
_RIGHT = ["  *  ", "   * ", "*****", "   * ", "  *  "]

for row in range(5):
    for i in _X:
        if i == "U":
            print(_UP[row], end=" ")
        elif i == "D":
            print(_DOWN[row], end=" ")
        elif i == "L":
            print(_LEFT[row], end=" ")
        elif i == "R":
            print(_RIGHT[row], end=" ")
    print()
