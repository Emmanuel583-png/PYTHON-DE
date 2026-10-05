raw_line = " Amara , 300 , 0 "
line  = raw_line.split(",")

name = line[0].strip()
level = line[1].strip()
body_count= line[2].strip()

print(F"{name} is a {level} level student with a body count of {body_count}")

#another way
raw_line = " Amara , 300 , 0 "

name_, level_, body_count_ = raw_line.split(",")
print(f"{name_.strip()} is a {level_.strip()} level student with a body count of {body_count_.strip()}")