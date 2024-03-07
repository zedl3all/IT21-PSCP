"""Socks"""

def main():
    """Socks"""
    sock = str(input())
    csock = {}
    for i in sock:
        if i not in csock:
            csock[i] = 1
        else:
            csock[i] += 1
    outsock = []
    for name, data in csock.items():
        even = data // 2
        for i in range(even):
            predata = name*2
            outsock.append(predata)
    outsock.sort()
    if not outsock:
        print("None")
    else:
        output = ""
        for i in outsock:
            output += i+" "
        print(output)
    print(len(outsock))
main()
