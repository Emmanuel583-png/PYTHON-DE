a_user_role_string: str = "ADMIN"
an_account_status: str = "suspended"
a_numeric_attempt: int = 3


status_ok =  an_account_status != "suspended"

role_or_attempt_ok = (a_user_role_string == "ADMIN") or (a_numeric_attempt < 3)
grant_access = status_ok and role_or_attempt_ok

print(status_ok)
print(role_or_attempt_ok)
print(f"if it is false then no access bro: {grant_access}")

#another way
def bs(role,status,attempt):
    return (status != "suspended") and (role == "admin" or attempt < 3)

#demo attempt
def check_access(role, status, attempts):
    return (status.upper() != "SUSPENDED") and (role == "ADMIN" or attempts < 3)



user1 = check_access("ADMIN", "suspended", 3)


user2 = check_access("USER", "ACTIVE", 2)

user3 = check_access("USER", "ACTIVE", 5)

print(f"User 1 Access: {user1}")
print(f"User 2 Access: {user2}")
print(f"User 3 Access: {user3}")