"""T-score"""
import math

def standardev(student, allstudent):
    """Standard Deviation"""
    precal = []
    for i in allstudent:
        precal.append(int(i)**2)
    cal = math.sqrt(((student*(sum(precal)))-sum(allstudent)**2)/(student*(student-1)))
    return cal

def zscore(student, allstudent):
    """Z-Score"""
    avgstudent = sum(allstudent)/student
    for i in allstudent:
        cal = (i-avgstudent)/standardev(student, allstudent)
        print("%.2f" % (50+(10*cal)))

def getdata():
    """T-score"""
    student = int(input())
    _ = int(input())
    allstudent = []
    for _ in range(student):
        score = int(input())
        allstudent.append(score)
    zscore(student, allstudent)

getdata()
