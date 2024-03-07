"""[Recommended] Dart"""
import math

def cal(location):
    """cal"""
    return math.sqrt(((int(location[0])-0)**2)+((int(location[1])-0)**2))

def main():
    """main"""
    dart = int(input())
    point = 0
    for _ in range(dart):
        location = str(input())
        calcu = cal(location.split())
        if calcu <= 2:
            point += 5
        elif calcu <= 4:
            point += 4
        elif calcu <= 6:
            point += 3
        elif calcu <= 8:
            point += 2
        elif calcu <= 10:
            point += 1
    print(point)
main()
