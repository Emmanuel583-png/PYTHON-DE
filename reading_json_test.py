import json 

with open('students2.json') as file:
    students = json.load(file)
for student in students:
    print(students)