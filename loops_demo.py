# standard range loop
for i in range(1, 6):
    print(i)

# loop control with break/continue
numbers = [10, 25, -5, 30, 999, 40]
for num in numbers:
    if num < 0:
        continue  # skip negative numbers
    if num == 999:
        break     # stop looping if sentinel value 999 is hit
    print(f"Processing: {num}")