"""Hamming"""

def main(str1, str2):
    """Hamming"""
    count = 0
    for i, _ in enumerate(str1):
        if str1[i] != str2[i]:
            count += 1
    print(count)
main(input(), input())
