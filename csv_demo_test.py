import csv

csv_file = "warehouse_inventory.csv"

header = ["item", "quantity", "price"]

row = [
    ["laptop", "15", "1200"],
    ["google_pixel", "90", "200"]

]

with open(csv_file, "w", newline= "") as file:
    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(row)

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for read in reader:
        print(read)