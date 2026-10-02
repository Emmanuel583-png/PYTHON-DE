# 1. Define the function without any dictionary
def format_user_record(username, score, status="PENDING"):
    # Clean the string (remove spaces and convert to small letters)
    clean_name = username.strip().lower()
    
    # Return a clean formatted string instead of a dictionary
    return f"User: {clean_name} | Score: {score} | Status: {status}"


# 2. Call the function without passing a status (uses default "PENDING")
user_1 = format_user_record(" Emmanuel ", 85)

# 3. Call the function with an explicit status ("APPROVED")
user_2 = format_user_record(" AMARA ", 92, "APPROVED")


# 4. Print the returned strings
print(user_1)
print(user_2)