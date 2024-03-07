"""WordSequence II"""

def main():
    """word"""
    text1 = str(input())
    text2 = str(input())
    for i in range(max(len(text1), len(text2)) + 1):
        print(text2[:i] + text1[i:])
main()
