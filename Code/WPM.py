"""WPM"""

def kid(wpm):
    """kid"""
    if wpm < 11:
        return "Very Slow"
    if wpm >= 11 and wpm <= 20:
        return "Slow"
    if wpm >= 21 and wpm <= 30:
        return "Average"
    if wpm >= 31 and wpm <= 40:
        return "Fast"
    if wpm > 40:
        return "Very Fast"

def adult(wpm):
    """adult"""
    if wpm < 26:
        return "Very Slow"
    if wpm >= 26 and wpm <= 35:
        return "Slow/Beginner"
    if wpm >= 36 and wpm <= 45:
        return "Intermediate/Average"
    if wpm >= 46 and wpm <= 65:
        return "Fast/Advanced"
    if wpm >= 66 and wpm <= 80:
        return "Very Fast"
    if wpm > 80:
        return "Insane"

def main():
    """WPM"""
    age = str(input())
    score = int(input())
    if age == "Kids":
        print(kid(score))
    else:
        print(adult(score))
main()
