"""CaesarV1"""

def caesar():
    """caesardecrypt"""
    shift = int(input())
    text = str(input())
    output = ""
    for i in text:
        if i.isalpha():
            lower = i.lower()
            decode = chr(((ord(lower) - ord('a') + shift) % 26) + ord('a'))
            if i.isupper() is True:
                decode = decode.upper()
            output += decode
        else:
            output += i
    print(output)
caesar()
