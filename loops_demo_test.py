alist = [-75, 838, -959, 464, -23, 0, 37575, 8394, 62]

for ali in alist:
    if ali < 0:
        continue
    if ali == 0:
        break
    print(f"import:ant remaining numbers -> {ali} ")

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

transactions = [120, -50, 450, -10, 9999, 300, -25]

for transaction in transactions:
    if transaction < 0:
        continue
    if transaction == 9999:
        break
    print(f"valid transaction: {transaction}")

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

countup = 3
while countup <= 3:
    print(countup)
    countup += 1