"""SurprisingVote"""

_VOTE = float(input())
_HIGH = float(input())

_TWO = min(_VOTE - _HIGH, _HIGH)
_LOW = _VOTE - _HIGH - _TWO
if _HIGH - _LOW > 2:
    print("Surprising")
else:
    print("Not surprising")
