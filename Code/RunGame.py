"""RunGame"""

def main():
    """run"""
    number = str(input())
    number = number.split()
    if number == []:
        print(0)
    else:
        count = int(number[0])
        for i in range(len(number)-1):
            count += abs(int(number[i])-int(number[i+1]))
        print(count)
main()
