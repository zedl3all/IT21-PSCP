"""year"""
_X = int(input())

if (_X % 4 == 0 and _X % 100 != 0) or (_X % 400 == 0):
    print("Yes")
else:
    print("No")
