# --- STEP 1: DEFINE THE FUNCTION ---
def format_user_record(username, score, status="PENDING"):
    clean_name = username.strip().lower()
    user_dictionary = {
        "user": clean_name,
        "score": score,
        "status": status
    }
    return user_dictionary

# --- STEP 2: RUNNING CALL 1 ---
user_1 = format_user_record(" Emmanuel ", 85)

# --- STEP 3: RUNNING CALL 2 ---
user_2 = format_user_record(" AMARA ", 92, "APPROVED")

# --- STEP 4: PRINTING RESULTS ---
print(user_1)
print(user_2)