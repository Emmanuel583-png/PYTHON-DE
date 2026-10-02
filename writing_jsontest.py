import json

# Read the file
with open("students.json", "r") as file:
    students = json.load(file)

# Filter passing students
passed = []
for student in students:
    if student["score"] > 50:
        passed.append(student)

# Write results to new file
with open("passed.json", "w") as file:
    json.dump(passed, file, indent=4)

print("Done")