"""[Recommended] BloodDonation"""

def main():
    """main"""
    can = []
    age = int(input())
    weight = int(input())
    count = int(input())
    if age == 17 or (age >= 60 and age <= 70):
        consent = input()
    if age >= 17 and age <= 70:
        can.append(True)
        if age == 17 or age >= 60:
            if consent == "True":
                can.append(True)
            else:
                can.append(False)
    else:
        can.append(False)
    if weight >= 45:
        can.append(True)
    else:
        can.append(False)
    if count == 0:
        if age <= 55:
            can.append(True)
        else:
            can.append(False)
    return can

def output(can):
    """output"""
    if False in can:
        print("No")
    else:
        print("Yes")

output(main())
