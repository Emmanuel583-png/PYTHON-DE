import csv

fieldnames = ["item", "quantity", "price"]

items = [
    {"item" : "lappy", "quantity" : "200", "price" : "2000"},
    {"item" : "samsung_8k_oled", "quantity" : "20", "price" : "9000"}
]

with open("just_doing_sum.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(items)


with open("just_doing_sum.csv", 'r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)


