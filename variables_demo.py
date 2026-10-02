# 1. Type Hinting: Explicitly declaring expected types
student_name: str = "Emmanuel"
raw_gpa_input: str = "3.75"  # Incoming data from a CSV is always a string!
is_active: bool = True
missing_field: str | None = None # Explicitly allowing missing data

# 2. Type Casting (Conversion)
# Uncommenting the line below will crash Python with a TypeError:
# calculation = raw_gpa_input + 0.25 

parsed_gpa: float = float(raw_gpa_input)
updated_gpa: float = parsed_gpa + 0.05

# 3. Dynamic Inspection
print("--- Type Inspection ---")
print(f"raw_gpa_input type: {type(raw_gpa_input)}")
print(f"parsed_gpa type:    {type(parsed_gpa)}")
print(f"Updated GPA Value:  {updated_gpa}")

# 4. Handling None Values Safely
if missing_field is None:
    print("Warning: Missing field detected! Setting default...")
    missing_field = "UNKNOWN"