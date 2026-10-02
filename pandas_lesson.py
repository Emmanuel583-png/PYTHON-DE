import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(df['name'])
print(df[["level", "score"]])

#filtering 
passed = df[df['score'] > 50]
print(passed)

passed.to_csv("passed_students.csv", index=False) 