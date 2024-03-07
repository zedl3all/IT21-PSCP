"""Phasmophobia"""

def inputdata(clue1, clue2, clue3):
    """inputdata"""
    for _ in range(3):
        if clue2 == "No evidence":
            clue2 = clue3
        if clue1 == "No evidence":
            clue1 = clue2
        if clue3 == "No evidence":
            clue3 = clue1
    return clue1, clue2, clue3

def main(clue):
    """Phsamo"""
    ghost = {"Banshee":["EMF Level 5", "Fingerprints", "Freezing Temperatures"],
             "Demon":["Ghost Writing", "Spirit Box", "Freezing Temperatures"],
             "Jinn":["EMF Level 5", "Spirit Box", "Ghost Orb"],
             "Mare":["Spirit Box", "Freezing Temperatures", "Ghost Orb"],
             "Oni":["EMF Level 5", "Ghost Writing", "Spirit Box"],
             "Phantom":["EMF Level 5", "Freezing Temperatures", "Ghost Orb"],
             "Poltergeist":["Fingerprints", "Spirit Box", "Ghost Orb"],
             "Revenant":["EMF Level 5", "Ghost Writing", "Fingerprints"],
             "Shade":["EMF Level 5", "Ghost Writing", "Ghost Orb"],
             "Spirit":["Ghost Writing", "Spirit Box", "Fingerprints"],
             "Wraith":["Spirit Box", "Fingerprints", "Freezing Temperatures"],
             "Yurei":["Ghost Writing", "Freezing Temperatures", "Ghost Orb"]}
    preghost = set()
    ghostcheck = False
    outghost = []
    if clue[0] == "No evidence" and clue[1] == "No evidence" and clue[2] == "No evidence":
        ghostsort = list(ghost.keys())
        ghostsort.sort()
        for i in ghostsort:
            print(i)
    else:
        for keyword, item in ghost.items():
            if clue[0] in item:
                preghost.add(keyword)
            if clue[1] in item:
                preghost.add(keyword)
            if clue[2] in item:
                preghost.add(keyword)
        for i in preghost:
            if clue[0] in ghost[i] and clue[1] in ghost[i] and clue[2] in ghost[i]:
                outghost.append(i)
                ghostcheck = True
        if ghostcheck is False:
            print("Not yet discovered")
        outghost.sort()
        for i in outghost:
            print(i)

main(inputdata(str(input()), str(input()), str(input())))
