import csv
import json

passed_students = []
#read student that are in csv module
with open("school_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        score = int(row['score'])
        if score > 50: #filtering for students
            row['status'] = "pass" #passing status
            passed_students.append(row)

with open("pipeline_output.json", "w") as json_file:
    json.dump(passed_students, json_file, indent=4)

print(f'{len(passed_students)} students passed')  

