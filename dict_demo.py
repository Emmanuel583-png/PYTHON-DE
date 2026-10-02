# Raw student record missing the 'score' key
raw_student: dict = {
    "name": "Emmanuel",
    "department": "Physics",
    "level": 300
}

# 1. Unsafe Access: This line would CRASH your pipeline with KeyError
# score = raw_student["score"] 

# 2. Safe Access with .get(key, default_value)
score: int = raw_student.get("score", 0)  # Defaults to 0 if 'score' doesn't exist

# 3. Safe Mutation
raw_student["status"] = "ENROLLED"

# 4. Dictionary Comprehension (Filtering data inline)
scores: dict[str, int] = {"Math": 85, "Physics": 42, "Chemistry": 91}
# Only keep subjects where score is 50 or above
passing_scores: dict[str, int] = {subject:val for subject, val in scores.items() if val >= 50}

print("--- DICTIONARY INSPECTION ---")
print(f"Safely Retrieved Score: {score}")
print(f"Updated Student Dict:   {raw_student}")
print(f"Passing Subjects Only:  {passing_scores}")