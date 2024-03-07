"""iPhone 13 Again"""

_X = str(input())
_Y = str(input())

if _X == "iPhone 13 mini":
    if _Y == "128 GB":
        print("25900")
    elif _Y == "256 GB":
        print("29900")
    elif _Y == "512 GB":
        print("37900")
    else:
        print("Not Available")
elif _X == "iPhone 13":
    if _Y == "128 GB":
        print("29900")
    elif _Y == "256 GB":
        print("33900")
    elif _Y == "512 GB":
        print("41900")
    else:
        print("Not Available")
elif _X == "iPhone 13 Pro":
    if _Y == "128 GB":
        print("38900")
    elif _Y == "256 GB":
        print("42900")
    elif _Y == "512 GB":
        print("50900")
    elif _Y == "1 TB":
        print("58900")
    else:
        print("Not Available")
elif _X == "iPhone 13 Pro Max":
    if _Y == "128 GB":
        print("42900")
    elif _Y == "256 GB":
        print("46900")
    elif _Y == "512 GB":
        print("54900")
    elif _Y == "1 TB":
        print("62900")
    else:
        print("Not Available")
else:
    print("Not Available")
