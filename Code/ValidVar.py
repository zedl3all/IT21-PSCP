"""ValidVar"""

_X = int(input())

for i in range(_X):
    _RESULT = "Valid"
    _Y = str(input())
    _Y = _Y.strip()
    if _Y[0].isnumeric():
        _RESULT = "Invalid"
    elif _Y == "if" or _Y == "else" or _Y == "elif" or _Y == "while" or _Y == "for" or\
        _Y == "True" or _Y == "False" or _Y == "continue" or _Y == "break":
        _RESULT = "Invalid"
    elif _Y == "return" or _Y == "is" or _Y == "in" or _Y == "and" or\
        _Y == "or" or _Y == "from" or _Y == "as" or _Y == "pass" or\
        _Y == "not" or _Y == "def" or _Y == "None":
        _RESULT = "Invalid"
    else:
        for j in range(len(_Y)):
            if _Y[j] == " ":
                _RESULT = "Invalid"
                break
            elif _Y[j].isalpha() == False and _Y[j].isnumeric() == False and _Y[j] != "_":
                _RESULT = "Invalid"
                break
    print(_RESULT)
