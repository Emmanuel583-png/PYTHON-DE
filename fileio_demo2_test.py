def log_error(service_name, error_code):
    with open("server_errors.txt", "a") as file:
        file.write(f"[ERROR] {service_name} returned code {error_code} \n")

first = log_error("1", "204")
second = log_error("2", "204")


with open("server_errors.txt", "r") as file:
    for line in file:
        print(line.strip())