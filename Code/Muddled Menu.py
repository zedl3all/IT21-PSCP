"""Muddled Menu"""

def menu():
    """menu"""
    food = []
    while True:
        word = str(input())
        if word == "DONE":
            break
        elif word == "CLOSED":
            food = []
            break
        elif word == "SOMETHING'S WRONG":
            food = []
        elif word.startswith("Can't do:"):
            word = word[10:]
            food.remove(word)
        else:
            word = word.split(" #")
            if word[1].isnumeric():
                food.insert(int(word[1])-1, word[0])
            else:
                food.append(word[0])
    print("Full Course:", food, "Reversed:", food[::-1])
menu()
