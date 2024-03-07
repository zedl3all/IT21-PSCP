"""GCD_v1"""

def gcd():
    """gcd"""
    number1 = int(input())
    number2 = int(input())
    if number1 == 0:
        print(number2)
    elif number2 == 0:
        print(number1)
    else:
        minnumber = min(number1, number2)
        output = 0
        for i in range(1, minnumber+1):
            if number1%i == 0 and number2%i == 0:
                output = i
        print(output)
gcd()
