"""PH"""

def main():
    """PH"""
    chemical = float(input())
    if chemical >= 0 and chemical < 7:
        print("acidic")
    elif chemical == 7:
        print("neutral")
    elif chemical > 7 and chemical <= 14:
        print("akaline")
    else:
        print("error")
main()
