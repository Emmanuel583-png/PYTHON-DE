import csv

with open("students.csv", "r") as file:
    reader= csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is a {row['level']} level student")