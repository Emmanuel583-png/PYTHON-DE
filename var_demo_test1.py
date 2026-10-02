raw_student_id: str ="10492"
raw_unit_score: str ="88.5"
raw_enrollment_status: str = "true"

student_id: int = int(raw_student_id)
unit_score: float = float(raw_unit_score) + 5.0
enrollment_status: bool = raw_enrollment_status == "true"

print(f"STUDENT_ID: {student_id} | {type(student_id)}")
print(f"UNIT_SCORE: {unit_score} | {type(unit_score)}")
print(f"Enrolled: {enrollment_status} | {type(enrollment_status)}")