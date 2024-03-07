"""Helloooo"""

def main():
    """Helloooo"""
    word = str(input())
    last = word[-1:]
    want = ["a", "e", "i", "o", "u",
            "A", "E", "I", "O", "U"]
    if last in want:
        print(word+last*3)
    else:
        spword = []
        for i in word:
            spword.append(i)
        #print(spword)
        for i in range(len(spword)-1, -1, -1):
            if spword[i] in want:
                spword[i] = spword[i]*4
                break
            #print(spword[i])
        out = ""
        for i in spword:
            out += i
        print(out)
main()
