"""[Midterm 2020] Shorten"""

def short():
    """short"""
    old_number = ""
    preout = ""
    prepreout = ""
    out = ""
    while True:
        number = int(input())
        if preout == "":
            preout += str(number)
        if old_number != "":
            if number == int(old_number)+1:
                preout += "-"
            else:
                preout += str(old_number)
                if out != "":
                    out += ", "
                for i in preout:
                    if i == "-":
                        if i not in prepreout:
                            prepreout += i
                    else:
                        prepreout += i
                out += prepreout
                prepreout = ""
                preout = str(number)
        old_number = str(number)
        if number == -1:
            break
    print(out)

short()
