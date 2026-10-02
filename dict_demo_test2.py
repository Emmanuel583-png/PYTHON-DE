user_session = {
    "username": "emmanuel_dev",
    "role": "admin"
}

timeout: int = user_session.get("timeout_seconds", 300)

user_session["is active"] = True
 #spent time thinking what how to infuse a bool, help!!


#Add a new key "is_active" with a boolean value True directly to user_session.

#enrollment_status: bool = raw_enrollment_status == "true"\

for field,value in user_session.items():
    print(f"FIELD: {field} -> VALUE: {value}")
    

