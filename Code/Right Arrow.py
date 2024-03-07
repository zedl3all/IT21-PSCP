"""Right Arrow"""
def main():
    """Right arrow"""
    wide = int(input())
    height = int(input())
    for i in range(height // 2):
        print(str(" " * i) + str("*" * wide))
    print(str(" " * (height//2)+"*" * wide))
    for i in range(height // 2):
        print(str(" " * ((height // 2)-i-1)) + str("*" * wide))
main()
