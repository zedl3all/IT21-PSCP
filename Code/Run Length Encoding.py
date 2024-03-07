"""Run Length Encoding"""

def main(inputstr):
    """"Encode"""
    output = ""
    count = 1
    for i in range(1, len(inputstr)):
        if inputstr[i] == inputstr[i-1]:
            count += 1
        else:
            output += str(count)+inputstr[i-1]
            count = 1
    output += str(count)+inputstr[-1]
    print(output)

main(str(input()))
