"""Jumping"""

def moreway(k):
    """MoreEntryway"""
    if k > 0:
        result = 1 + moreway(k-1)
        print("Output" + str(result))
        print("Output" + str(result))
        print("Output" + str(result))
    else:
        result = 0
    return result

moreway(4)
