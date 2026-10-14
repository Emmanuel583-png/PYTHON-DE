import csv

i = "subscriptions.csv"

header = ["username", "plan", "is_active"]


rows = [
    ["ade", "free", True],
    ["kann", "pro", False],
    ["kunle", "free", True],
    ["ada", "pro", False],
    ["adelede", "free", False],
    ["nana", "pro", True]
]

with open(i, "w", newline="") as file:
    data = csv.writer(file)
    data.writerow(header)
    data.writerows(rows)
