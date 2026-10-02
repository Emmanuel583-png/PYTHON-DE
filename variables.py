
name = 'Emmanuel'
level = 200
social_security = 3.75
is_student = True


print(name)
print(level)
print(social_security)
print(is_student)

scores = [85, 92, 78, 95,60]
for score in scores:
    print(score)

scores = [85, 92, 78, 95, 60]
scores.append(100) #adds 100 to the end of the scores
scores.remove(78) #removes 78 from the scores
scores.sort() #sorts the list from lowest to highest

print(scores)

courses = ['maths', 'english', 'physics', 'crs', 'agric']
print(courses[0])
print(courses[-1])

for course in courses:
    print(course)