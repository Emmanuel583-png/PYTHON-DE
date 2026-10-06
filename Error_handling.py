def process_record(value):
    try:
        number = int(value)
        print(f"score: {number}")
    except ValueError:
        print(f"skipping invalid record: {value}")

records = ["85", "90", "invalid", "78", "none", "60"]
for record in records:
    process_record(record)

try:
    number: int = []
except ValueError:
    print("bad value")
else:
    print("conversion successful")
finally:
    print("this always runs")

try:
    result = int("Amara") / 0
except Exception as e:
    print(f"something went wrong: {e}")