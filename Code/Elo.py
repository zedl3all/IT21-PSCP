"""Elo"""

_RA = int(input())
_RB = int(input())
_TEAM = str(input())

if _TEAM == "A":
    _EA = 1/(1+(10**((_RB-_RA)/400)))
    print("%.2f" % _EA)
else:
    _EB = 1/(1+(10**((_RA-_RB)/400)))
    print("%.2f" % _EB)
