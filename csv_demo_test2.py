import csv

csv_file = "users_log.csv"

fieldnames = ["username", "role", "status"]

dd = [
    {"username" : "Osato", "role" : "playwright", "status" : "married"}, 
    {"username" : "Caleb", "role" : "director", "status" : "un-married"}
]

with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(dd)

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for read in reader:
        print(f"{read['username']} holds the role of {read['role']} and {read['status']}")