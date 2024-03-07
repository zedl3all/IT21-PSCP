"""FibonacciRecursionV1"""

def fibo(number):
    """FibonacciRecursion"""
    if number <= 1:
        return number
    else:
        return fibo(number-1)+fibo(number-2)

print(fibo(int(input())))
