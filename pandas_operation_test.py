import pandas as pd
df = pd.read_csv("students.csv")
df["status"] = df["score"].apply(lambda x: "pass" if x > 50 else "fail")
group = df.groupby("department")["score"].mean()
print(df.sort_values("score"))
print(group)

df.to_csv("final_students.csv", index=False)
