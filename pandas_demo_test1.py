import pandas as pd

company_overview = {
    "product" : ["shrimp", "lobster", "turkey", "quail_eggs"],
    "category" : ["sea_food", "sea_food", "meat", "eggs"],
    "price" : [120, 490, 300, 700],
    "quantity_sold" : [2, 5, 7, 10]
}

df = pd.DataFrame(company_overview)

df["total_revenue"] = df["price"] * df["quantity_sold"]


print(df)

sum_finding = df["total_revenue"].sum()
print(sum_finding)

rev_gen = df.groupby("category")["total_revenue"].mean()
print(rev_gen)