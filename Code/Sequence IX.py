"""ChristmasTree"""

_X = int(input())

for row in range(_X):
    for i in range(_X - row - 1):
        print("  ", end=" ")
    for i in range(row + 1):
        print("%02d" % (i + 1), end=" ")
    for i in range(row, 0, -1):
        print("%02d" % i, end=" ")
    print()
