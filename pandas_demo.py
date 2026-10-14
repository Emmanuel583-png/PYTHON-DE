import pandas as pd

data = {
    "server" : ["auth_api", "payment_api", "auth_api", "database"],
    "latency_ms" : [120, 450, 85, 600],
    "status" : ["ok", "slow", "ok", "slow"]
}

df = pd.DataFrame(data)

#printing first 2 rows 
print("---first 2 rows---")
print(df.head(2))

slow_internet = df[df['status'] == "slow"]
print(slow_internet)