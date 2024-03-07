"""LetterFrequency"""

def main():
    """LetterFrequency"""
    text = str(input())
    textdict = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            textdict[str(i)] = 0
    for i in text:
        if i.isalpha():
            textdict[str(i)] += 1
    print(max(textdict, key=textdict.get))
main()
