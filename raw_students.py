try:
    with open("raw_students.txt", "r") as file:
        for line in file:
            #split the line by comma
            parts = line.split(",")
            
            #strip and clean each field
            name = parts[0].strip().title()
            level = parts[1].strip()
            score = parts[2].strip()
            
            #check pass or fail
            if int(score) > 50:
                status = "Pass"
            else:
                status = "Fail"
            
            #print the result
            print(f"{name} | Level: {level} | Score: {score} | Status: {status}")

except FileNotFoundError:
    print("File not found. Please check the file path.")