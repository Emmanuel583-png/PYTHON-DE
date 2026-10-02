print (5 > 3) #true
print (3 > 5) #false
print ('a' == 'a') #true

level = 200
body_count = 0

print(level > 100 and body_count == 0) #true
print (level > 300 or body_count == 0) #true 
print (not body_count == 0) #false

is_eligible = level >= 200 and body_count == 0
print(is_eligible) #true 

level = 300
body_count = 0
attendance = 85

can_graduate = level >= 300 and body_count == 0 and attendance >= 75
print(can_graduate)
