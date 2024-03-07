"""AlmostMean"""
def almost():
    """alomost"""
    number = int(input())
    cal = 0
    lista = []
    listb = []
    for i in range(number):
        grade = str(input())
        grage1 = grade.split()
        cal += float(grage1[1])
        lista.append(float(grage1[1]))
        listb.append(grade)
    avg = cal/number
    #print(avg)
    listnum = []
    for i in lista:
        if i <= avg:
            listnum.append(i)
    #print(listnum)
    listless = []
    for i in listnum:
        listless.append(abs(avg-i))
    #print(min(listless))
    #print(listless.index(min(listless)))
    #print(listnum[listless.index(min(listless))])
    #print(lista.index(listnum[listless.index(min(listless))]))
    print(listb[lista.index(listnum[listless.index(min(listless))])])
almost()
