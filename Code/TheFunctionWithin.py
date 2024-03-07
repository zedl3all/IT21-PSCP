"""TheFunctionWithin"""


_A = float(input())
_B = float(input())
_C = float(input())
_D = float(input())


def function(xebra):
    """function"""
    return 2 * xebra


def gamma(xebra):
    """function"""
    return (3 * xebra**4) - (xebra**3) + (2 * xebra**2) + 10


def eta(xebra, yeeraf, zeebra):
    """function"""
    return ((zeebra + xebra)**2) - (xebra * yeeraf) + (yeeraf**2)


def iota(ant, ball, cat, dog):
    """function"""
    return (ant**2 + ball**2 - cat**2) / ((dog**2) - (2 * ant * dog) + (2 * ant))


print(function(function(_A)))
print(gamma(function(_A - _B)))
print(eta(function(_A + _B), function(_A + _C), gamma(function(_D**2))))
print(iota(eta(function(_A + _B),
               function(_A - _C),
               gamma(function(_D**2))),
           gamma(function(_A - _B)),
           function(function(function(function(function(_C))))),
           _D**8))
