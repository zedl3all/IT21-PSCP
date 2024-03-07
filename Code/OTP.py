"""OTP"""

def check4(otp, dictotp):
    """check4number"""
    if len(otp) == 4:
        count = 0
        for i in dictotp.values():
            if i == 2:
                count += 1
        if count == 1:
            print("Valid")
        else:
            print("Invalid")

def check6(otp, dictotp):
    """check6number"""
    if len(otp) == 6:
        count3 = 0
        count2 = 0
        for i in dictotp.values():
            if i == 3:
                count3 += 1
            if i == 2:
                count2 += 1
        if count3 == 1:
            print("Valid")
        elif count2 == 2:
            print("Valid")
        else:
            print("Invalid")

def check8(otp, dictotp):
    """check8number"""
    if len(otp) == 8:
        count3 = 0
        count2 = 0
        for i in dictotp.values():
            if i == 3:
                count3 += 1
            if i == 2:
                count2 += 1
        if count3 == 2:
            print("Valid")
        elif count2 == 3:
            print("Valid")
        else:
            print("Invalid")

def main():
    """OTP"""
    while True:
        otp = str(input())
        dictotp = {}
        if otp == "0":
            break
        for i in otp:
            dictotp[i] = dictotp.get(i, 0) + 1
        check4(otp, dictotp)
        check6(otp, dictotp)
        check8(otp, dictotp)

main()
