"""Run Length Encoding"""

def main(message):
    "nub"
    liststr = []
    listint = []
    preint = ""
    output = ""
    for i in message:
        if i.isnumeric():
            preint = preint + i
        elif i.isalpha():
            liststr.append(i)
            listint.append(preint)
            preint = ""
    for i in range(len(liststr)):
        output = output+(str(liststr[i])*int(listint[i]))
    print(output)

main(message=str(input()))
