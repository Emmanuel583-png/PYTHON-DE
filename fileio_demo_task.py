file_name = "order.txt"

def two_piece(order_id, status):
    with open(file_name, "a") as file:
        file.write(f"ORDER: {order_id} | STATUS: {status} \n")

case_1 = two_piece("ORD101", "SUCCESS")
case_2 = two_piece("ORD102", "PENDING")
case_3 = two_piece("ORD103", "FAILED")

try:
    with open(file_name, "r") as file:
        for line in file:
            print(f"ion: {line.strip()}??")
except FileNotFoundError:
    print(f"see that?: {file_name} > you messed up there buddy")


