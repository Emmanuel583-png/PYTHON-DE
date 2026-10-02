import csv

students = [
    {"name": "Emmanuel", "level": "300", "score": "85"},
    {"name": "Amara", "level": "100", "score": "91"},
]

with open("passed_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "level", "score"])
    writer.writeheader()
    writer.writerows(students)