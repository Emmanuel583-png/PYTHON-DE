with open ("pipeline_status.txt", "a") as file:
    file.write("BATCH01: COMPLETED \n")
    file.write("BATCH02: COMPLETED \n")

try:
    with open("pipeline_status.txt", "r") as file:
        for line in file:
            print(f"successfully read: {line.strip()}")
except FileNotFoundError:
    print(f"bruhh you have got bigger fish to fry")