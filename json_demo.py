import json

file_name = "student_profile.json"

profile = {
    "name" : "Osakpolo",
    "level" : "400",
    "course" : ["topology", "poetry", "art"],
    "is_active" : True
}

with open(file_name, "w") as file:
    json.dump(profile, file, indent=4)

with open(file_name, "r") as file:
    data = json.load(file)
    print(data)
    print(f"only name: {profile["name"]}")