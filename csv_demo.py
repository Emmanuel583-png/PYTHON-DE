import csv

header = ["name", "score", "status"]

row = [
    ["Anthony", "37", "Failed"],
    ["Ray", "54", "passed"],
    ["Chris", "100", "passed"]

]

with open("student_scores.csv", "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(row)

file_name = "student_scores.csv"

with open(file_name, "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

    
    