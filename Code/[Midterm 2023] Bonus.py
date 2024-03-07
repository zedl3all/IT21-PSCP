"""[Midterm 2023] Bonus"""

_SALARY = int(input())
_YEAR = int(input())
_MONTH = int(input())

if _MONTH >= 10:
    _YEAR += 1
if _YEAR >= 20:
    _YEAR = 20
_BONUS = _SALARY * _YEAR
if _BONUS < 5000:
    _BONUS = 5000
if _BONUS > 1000000:
    _BONUS = 1000000
print(_BONUS)
