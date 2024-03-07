"""OneTwo"""

def fibo(number):
    """FibonacciRecursion"""
    output = ""
    if number > 0 and number < 3:
        return str(number)
    else:
        output += fibo(number-1)+fibo(number-2)
    return output

print(fibo(int(input())))
