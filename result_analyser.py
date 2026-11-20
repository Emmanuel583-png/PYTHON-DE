import json 
import sqlite3
import pandas as pd

student = {
    "name" : ["anthony", "tola", "fola", "laju", "gabriel"],
    "level" : [400, 400, 400, 400, 400],
    "test_score/CA" : [30, 0, 12, 29, 10],
    "attendance" : [10, 6, 8, 3, 8],
    "exam_score" : [45, 30, 50, 17, 4]
}

still_raw = pd.DataFrame(student)

still_raw['total'] = still_raw['test_score/CA'] + still_raw['attendance'] + still_raw['exam_score']

def grades_asi(total):
    if total >= 70:
        return "A"
    elif total >= 60:
        return "B"
    elif total >= 50:
        return "C"
    elif total >= 45:
        return "D"
    elif total >= 40:
        return "E"
    else:
        return "F"

still_raw['grade'] = still_raw['total'].apply(grades_asi)

still_raw['status'] = still_raw['total'].apply(lambda x: "passed" if x > 50 else "fail")

print(still_raw)



