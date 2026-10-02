with open("students.txt", "w") as file:
    file.write("Emmanuel, 300, 0\n")
    file.write("Tolu, 200, 1\n")
    file.write("Amara, 100, 2\n")
print("successfully written this batch of students")


with open("students.txt", "a") as file:
    file.write("Ugo, 400, 3\n")

try:
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Oops! i am not sure any file like that is in this computer")

with open("foods.txt", "w") as file:
    file.write("spagetti\n")
    file.write("beans\n")
    print("fav foods!")

with open("foods.txt", "a") as file:
    file.write("noodles\n")

try:
    with open("food.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("oopsie daizy")