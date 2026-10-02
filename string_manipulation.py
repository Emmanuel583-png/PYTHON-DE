name =  " emmanuel "

print(name.strip()) #remove unnecessary spacing before starting each words or sentence
print(name) #just brings that shii out 
print(name.upper()) #makes the whole word capital letters  
print(name.lower()) #makes the whole word lower case
print(name.title()) #makes the first letter in capital letters 

line = "Emmanuel,200,5"
parts = line.split(",")
print(parts)

words = ["I", "am", "studying", "SQL"]
sentence = "".join(words)
print(sentence)

text = "Emmanuel is a 200 level student"
print(text.replace("200", "300"))

name = "Tolu"
level = 200
print(f"{name} is a {level} level student") 

email = "emmanuel@gmail.com"
print(email.startswith("emm"))
print(email.endswith(".com"))
print("gmail" in email)

raw_line = "Amara, 300, 0"
splitting= raw_line.split(",")

name = splitting[0].strip()
level = splitting[1].strip()
body_count = splitting[2].strip()
print(f"{name} is a {level} level student with a body count of {body_count}")

