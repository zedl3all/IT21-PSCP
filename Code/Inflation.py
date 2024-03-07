"""inflation"""

def main(price, year):
    """inflation cal"""
    price = int(price*100)
    for _ in range(year):
        price = (price*10381)//10000
    print(("%d" % (price//100)) + "." + ("%02d" % (price%100)))
main(float(input()), int(input()))
