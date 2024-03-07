"""IP Address"""

def main():
    """IP Address"""
    ipv4 = str(input())
    ipv4 = ipv4.split(".")
    check = False
    if len(ipv4) != 4:
        print("Invalid IPv4 address")
    else:
        for i in ipv4:
            if not i.isnumeric():
                print("Invalid IPv4 address")
                check = True
                break
            if int(i) > 255:
                print("Invalid IPv4 address")
                check = True
                break
        if check is False:
            output = ""
            for i in ipv4:
                output += str(int(i))+"."
            print(output[:-1])
main()
