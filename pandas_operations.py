#sortinng values()
import pandas as pd
df = pd.read_csv("students.csv")
print(df.sort_values("score")) #sorting the scores from highest to the lowest
print(df.sort_values("score", ascending=False)) #sorting the scores from lowest to the highest

grouped = df.groupby("department")['score'].mean()
print(grouped)

