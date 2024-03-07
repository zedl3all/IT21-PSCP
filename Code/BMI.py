"""BMI"""

_A = []


def moreway(k):
    """MoreEntryway"""
    if k > 0:
        result = 1 + moreway(k - 1)
        cococo = input()
        _A.append(cococo)
    else:
        result = 0
    return result


moreway(15)


def bmi(i):
    """BMI"""
    if i > 0:
        result = 1 + bmi(i - 1)
        print(str(_A[0]) + "'s", " BMI =", "%.2f" %
              (float(_A[1]) / ((float(_A[2]) / 100)**2)))
        _A.pop(0)
        _A.pop(0)
        _A.pop(0)
    else:
        result = 0
    return result


bmi(5)


# print(_A)
# print(_B)
