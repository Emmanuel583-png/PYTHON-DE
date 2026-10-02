student = {
    'name' : 'Hitler',
    'age' : 21,
    'body_count' : 4

}

print(student['name']) #ion know what tf im doing rn might delete later or some shii

student['University'] = 'Uniben' 

print(student['name'])
print(student['body_count'])
print(student['age'])
print(student['University'])

for key, value in student.items():
    print(f"{key}: {value}")
#.items() gives you both the key and the value on each round

my_profile = {
    'name' : 'osas',
    'age' : '14',
    'level' : 200,
    'school' : 'urhobo_college',
    'is_student' : True
    
}

for key, value in my_profile.items():
    print(f"{key} : {value}")


#1    #difference between dictionary and list is that in lists, you get diffent values attached to just one value like this 
    #student = ["name", 886, 993] 
    #but in dictionaries a key is head and value attached to other variables is used like 
    #student = {
        #'name' : 'hitler' 
        # 'age' : 11 where values is easily distinguishable and can be applied fairly easily
    #}

#2. player["title"] = "GM"
#3. confused??