def format_user_record (user_name,score, status = "pending"):
    converted_name = user_name.strip().lower()
    user_dict = {
        "user": converted_name,
        "score": score,
        "status": status
    }
    return user_dict

#default status
user_1 = format_user_record("emmanuel", 85)

#tweaked 
user_2 = format_user_record("amara", 92, status = "approved!")

print(user_1)
print(user_2)