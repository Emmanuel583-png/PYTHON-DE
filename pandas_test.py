import pandas as pd 

df = pd.read_csv("students.csv")
print(df.shape)

#filtering
df_filtering = df[df['score'] > 50]
print(df_filtering)

df_filtering.to_csv("pandas_passed.csv", index=False)