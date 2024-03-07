"""CoinChangev1"""

def main():
    """change"""
    money = int(input())
    coin = 0
    count = 0
    while coin != money:
        if coin + 25 <= money:
            coin += 25
            count += 1
        elif coin + 10 <= money:
            coin += 10
            count += 1
        elif coin + 5 <= money:
            coin += 5
            count += 1
        elif coin + 1 <= money:
            coin += 1
            count += 1
    print(count)
main()
