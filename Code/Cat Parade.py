"""Cat Parade"""

def main():
    """cat"""
    allcat = []
    while True:
        cat = str(input())
        if cat == "END":
            break
        listcat = cat.split(",")
        for position, item in enumerate(listcat):
            if item.startswith(" "):
                listcat[position] = listcat[position][1:]
            if listcat[position] == "IT'S A DOG":
                allcat.pop()
            else:
                allcat.append(listcat[position])
    catdict = {}
    for i in allcat:
        catdict[i] = catdict.get(i, 0) + 1
    presortcat = list(catdict.keys())
    presortcat.sort()
    sortcat = {i: catdict[i] for i in presortcat}
    for key, item in sortcat.items():
        print(key, (allcat.index(key)+1), item)

main()
