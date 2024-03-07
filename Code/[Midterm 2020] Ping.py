"""[Midterm 2020] Ping"""

_L1 = str(input())
_L2 = str(input())
_L3 = str(input())
_L4 = str(input())
_L5 = str(input())
_L6 = str(input())
_L7 = str(input())

_CHECK = False
_PREIP = ""
_IP = ""

###_GETIP###
if "[" in _L3 or "]" in _L3:
    for i in _L3:
        if i == "[":
            _CHECK = True
        if i == "]":
            _CHECK = False
        if _CHECK is True:
            _IP += i
    _IP = _IP[1:]
else:
    for i in _L3:
        if i.isnumeric() or i == ".":
            _PREIP += i
        else:
            _PREIP += " "
    _PREIP = _PREIP.strip()
    for i in _PREIP:
        if i.isspace():
            break
        else:
            _IP += i
###_GETIP###

###COUNT_RECEIVE###
_COUNT = 0
if "Reply" not in _L4:
    _COUNT += 1
if "Reply" not in _L5:
    _COUNT += 1
if "Reply" not in _L6:
    _COUNT += 1
if "Reply" not in _L7:
    _COUNT += 1
###COUNT_RECEIVE###

###GET_MIN_MAX###
_TL4 = ""
_TL5 = ""
_TL6 = ""
_TL7 = ""

_CHECK = False
_PRET = tuple()
_PREWORD = ""
#LINE4
if "time" in _L4:
    for i in _L4:
        if i.isspace():
            _PRET += (_PREWORD,)
            _PREWORD = ""
        else:
            _PREWORD += i
    _PRET += (_PREWORD,)
    _PREWORD = ""
    for i in _PRET:
        if "time" in i:
            _TL4 += i
    _PRET = tuple()
#LINE5
if "time" in _L5:
    for i in _L5:
        if i.isspace():
            _PRET += (_PREWORD,)
            _PREWORD = ""
        else:
            _PREWORD += i
    _PRET += (_PREWORD,)
    _PREWORD = ""
    for i in _PRET:
        if "time" in i:
            _TL5 += i
    _PRET = tuple()
#LINE6
if "time" in _L6:
    for i in _L6:
        if i.isspace():
            _PRET += (_PREWORD,)
            _PREWORD = ""
        else:
            _PREWORD += i
    _PRET += (_PREWORD,)
    _PREWORD = ""
    for i in _PRET:
        if "time" in i:
            _TL6 += i
    _PRET = tuple()
#LINE7
if "time" in _L7:
    for i in _L7:
        if i.isspace():
            _PRET += (_PREWORD,)
            _PREWORD = ""
        else:
            _PREWORD += i
    _PRET += (_PREWORD,)
    _PREWORD = ""
    for i in _PRET:
        if "time" in i:
            _TL7 += i
    _PRET = tuple()
_TL4 = _TL4[4:]
_TL5 = _TL5[4:]
_TL6 = _TL6[4:]
_TL7 = _TL7[4:]

if _TL4 != "":
    if _TL4[0] == "<":
        _TL4 = "0"
    else:
        _TL4 = _TL4[1:]
        _TL4 = _TL4[:-2]

if _TL5 != "":
    if _TL5[0] == "<":
        _TL5 = "0"
    else:
        _TL5 = _TL5[1:]
        _TL5 = _TL5[:-2]

if _TL6 != "":
    if _TL6[0] == "<":
        _TL6 = "0"
    else:
        _TL6 = _TL6[1:]
        _TL6 = _TL6[:-2]

if _TL7 != "":
    if _TL7[0] == "<":
        _TL7 = "0"
    else:
        _TL7 = _TL7[1:]
        _TL7 = _TL7[:-2]
#print(_TL4)
#print(_TL5)
#print(_TL6)
#print(_TL7)
_MIN = ""
_MAX = ""
_AVG = ""
if _TL4 == "" and _TL5 == "" and _TL6 == "" and _TL7 == "":
    print("Ping statistics for", _IP + ":")
    print("    Packets: Sent = 4,", "Received =", str(4-_COUNT)+",", "Lost =", \
        str(_COUNT) + " (" + (str(int((_COUNT/4)*100)) + "%"), "loss"+")"+ ",")
else:
    if _TL7 == "" and _TL6 != "" and _TL5 != "" and _TL4 != "":#L456
        _MIN = min(int(_TL4), int(_TL5), int(_TL6))
        _MAX = max(int(_TL4), int(_TL5), int(_TL6))
        _AVG = (int(_TL4) + int(_TL5) + int(_TL6))/3
    elif _TL6 == "" and _TL7 != "" and _TL5 != "" and _TL4 != "":#L457
        _MIN = min(int(_TL4), int(_TL5), int(_TL7))
        _MAX = max(int(_TL4), int(_TL5), int(_TL7))
        _AVG = (int(_TL4) + int(_TL5) + int(_TL7))/3
    elif _TL5 == "" and _TL6 != "" and _TL7 != "" and _TL4 != "":#L467
        _MIN = min(int(_TL4), int(_TL6), int(_TL7))
        _MAX = max(int(_TL4), int(_TL6), int(_TL7))
        _AVG = (int(_TL4) + int(_TL7) + int(_TL6))/3
    elif _TL4 == "" and _TL6 != "" and _TL5 != "" and _TL7 != "":#L567
        _MIN = min(int(_TL5), int(_TL6), int(_TL7))
        _MAX = max(int(_TL5), int(_TL6), int(_TL7))
        _AVG = (int(_TL5) + int(_TL7) + int(_TL6))/3
    elif _TL7 == "" and _TL6 == "" and _TL5 != "" and _TL4 != "":#L45
        _MIN = min(int(_TL4), int(_TL5))
        _MAX = max(int(_TL4), int(_TL5))
        _AVG = (int(_TL4) + int(_TL5))/2
    elif _TL7 == "" and _TL5 == "" and _TL6 != "" and _TL4 != "":#L46
        _MIN = min(int(_TL4), int(_TL6))
        _MAX = max(int(_TL4), int(_TL6))
        _AVG = (int(_TL4) + int(_TL6))/2
    elif _TL7 == "" and _TL4 == "" and _TL5 != "" and _TL6 != "":#L56
        _MIN = min(int(_TL6), int(_TL5))
        _MAX = max(int(_TL6), int(_TL5))
        _AVG = (int(_TL6) + int(_TL5))/2
    elif _TL7 != "" and _TL6 == "" and _TL5 == "" and _TL4 != "":#L47
        _MIN = min(int(_TL4), int(_TL7))
        _MAX = max(int(_TL4), int(_TL7))
        _AVG = (int(_TL4) + int(_TL7))/2
    elif _TL7 != "" and _TL6 == "" and _TL5 != "" and _TL4 == "":#L57
        _MIN = min(int(_TL5), int(_TL7))
        _MAX = max(int(_TL5), int(_TL7))
        _AVG = (int(_TL5) + int(_TL7))/2
    elif _TL7 != "" and _TL6 != "" and _TL5 == "" and _TL4 == "":#L67
        _MIN = min(int(_TL6), int(_TL7))
        _MAX = max(int(_TL6), int(_TL7))
        _AVG = (int(_TL6) + int(_TL7))/2
    elif _TL7 == "" and _TL6 == "" and _TL5 == "" and _TL4 != "":#L4
        _MIN = int(_TL4)
        _MAX = int(_TL4)
        _AVG = int(_TL4)
    elif _TL7 == "" and _TL5 != "" and _TL6 == "" and _TL4 == "":#L5
        _MIN = int(_TL5)
        _MAX = int(_TL5)
        _AVG = int(_TL5)
    elif _TL7 == "" and _TL6 != "" and _TL5 == "" and _TL4 == "":#L6
        _MIN = int(_TL6)
        _MAX = int(_TL6)
        _AVG = int(_TL6)
    elif _TL7 != "" and _TL5 == "" and _TL6 == "" and _TL4 == "":#L7
        _MIN = int(_TL7)
        _MAX = int(_TL7)
        _AVG = int(_TL7)
    elif _TL7 != "" and _TL5 != "" and _TL6 != "" and _TL4 != "":#L4567
        _MIN = min(int(_TL4), int(_TL5), int(_TL6), int(_TL7))
        _MAX = max(int(_TL4), int(_TL5), int(_TL6), int(_TL7))
        _AVG = (int(_TL4) + int(_TL5) + int(_TL6) + int(_TL7))/4
    print("Ping statistics for", _IP + ":")
    print("    Packets: Sent = 4,", "Received =", str(4-_COUNT)+",", "Lost =", \
        str(_COUNT) + " (" + (str(int((_COUNT/4)*100)) + "%"), "loss"+")"+",")
    print("Approximate round trip times in milli-seconds:")
    print("    Minimum =", str(_MIN)+'ms'+',', "Maximum =", \
        str(_MAX)+'ms'+',', "Average =", str(int(_AVG))+'ms')
###GET_MIN_MAX###
