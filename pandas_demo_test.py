import pandas as pd

df = pd.read_csv("subscriptions.csv")

print(df.columns)

pro_users = df[df[ 'plan'] == "pro"]

print(pro_users)


