"""PrasomSib"""

def prasom():
    """PrasomSib"""
    number = str(input())
    test = []
    while True:
        pretest = []
        for i in number:
            if sum(pretest) < 10:
                pretest.append(int(i))
            elif sum(pretest) > 10:
                pretest.pop()
                number = number[1:]
                break
            else:
                test.append(pretest)
                pretest = []
                number = number[1:]
                break
        if len(pretest) == len(number) and sum(pretest) < 10:
            break
        else:
            if sum(pretest) == 10:
                test.append(pretest)
                break
            if sum(pretest) > 10:
                pretest.pop()
                number = number[1:]
    #print(test)
    print(len(test))

prasom()
