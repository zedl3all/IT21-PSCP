"""isPrime (LARGER)"""
import math

def is_prime(number):
    """isPrime"""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

if is_prime(int(input())):
    print(True)
else:
    print(False)
