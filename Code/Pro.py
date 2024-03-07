"""Pro"""

def main():
    """pro"""
    mar4 = int(input())
    jai3 = int(input())
    huara = int(input())
    mar = int(input())
    if mar < mar4:
        print(mar*huara)
    else:
        pay1 = mar // mar4
        pay2 = mar % mar4
        pay = (pay1*jai3*huara)+(pay2*huara)
        print(pay)

main()
