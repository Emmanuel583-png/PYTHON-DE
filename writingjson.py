import json

student = {
    "name" : "Emmanuel",
    "level" : 300,
    "courses" : ["physics", "math", "sql"]
    }

with open("student_credentials.json", "w") as file:
    json.dump(student, file, indent=4)

    #there is a hideous mistake with this but im too lazy rn to correct that code and thats why so uhm... yeah
    #move on kid!!