import json

#reading for all the students 
with open("students.json", "r") as file:
    students = json.load(file)

#filter for the passed students 
passed =[]
for student in students:
    if student['score'] > 50:
        passed.append(student)
    

#filter for failed students
failed =[]
for student in students:
    if student['score'] < 50:
        failed.append(student)

#new file for failed and passed students
with open("failed_passed.json", "w") as file:
    json.dump({"passed": len(passed), "failed": len(failed)}, file, indent=4)
