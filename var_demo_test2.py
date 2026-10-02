raw_score_1: str = "45"
raw_score_2: str = "35"
raw_pass_cutoff: str = "70"

score_1: int = int(raw_score_1)
score_2: int = int(raw_score_2)

total_score = score_1 + score_2

cutoff: int = int(raw_pass_cutoff)
has_passed: bool = total_score >= cutoff 

print(F"TOTAL_SCORE: {total_score} | {type(total_score)}")
print(f"HAS_PASSED: {has_passed} | {type(has_passed)}")