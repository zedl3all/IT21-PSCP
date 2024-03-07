"""Calculator V2"""

def main(number):
    """Calculator V2"""
    out = ""
    if number == 1:
        print(number)
    else:
        for i in range(1, number+1):
            out += str(i)+"+"
        print(len(out))

main(int(input()))

def main2(number):
    total = number * (number+1) // 2
    print(total)
main2(int(input()))