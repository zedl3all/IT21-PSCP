"""ChristmasTree"""

def main(leaf, wood):
    """buildTree"""
    leaf = leaf*2
    for i in range(1, leaf, 2):
        print(("*"*i).center(leaf))
    for i in range(wood):
        print(("---").center(leaf))

main(leaf=int(input()), wood=int(input()))
