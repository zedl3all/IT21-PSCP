"""Day2011"""

def calculateday():
    """calculateday"""
    day = int(input())
    month = int(input())
    year = 2021
    if month < 3:
        month += 12
        year -= 1
    cal1 = year % 100
    cal2 = year // 100
    day_of_week = (day + 13 * (month + 1) // 5 + cal1 + cal1 // 4 + cal2 // 4 - 2 * cal2) % 7
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(days[day_of_week])
calculateday()
