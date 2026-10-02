import pandas as pd

# reading the file
df = pd.read_csv("university_data.csv")
print(df.shape)

# adding status column with two conditions
df["status"] = df.apply(lambda row: "Pass" if row["score"] > 50 and row["attendance"] > 60 else "Fail", axis=1)

# sort by score highest to lowest
print(df.sort_values("score", ascending=False))

# average score per department
getting_avg = df.groupby("department")["score"].mean()
print(getting_avg)

# save only passing students
passing = df[df["status"] == "Pass"]
passing.to_csv("final_report.csv", index=False)

# print counts
print(f"Passed: {len(df[df['status'] == 'Pass'])}")
print(f"Failed: {len(df[df['status'] == 'Fail'])}")