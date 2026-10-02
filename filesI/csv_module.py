import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is a {row['level']} level student")

import csv

students = [
    {"name": "Emmanuel", "level" "300" "body_count" "0"},
    {"name" "Tolu" "200" "body_count" "1"}
]