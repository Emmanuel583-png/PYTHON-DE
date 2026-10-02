import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        score = int(row['score'])
        if score > 50:
            print(f"{row["name"]} passed with a score of {row["score"]}")
