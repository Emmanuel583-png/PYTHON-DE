import pandas as pd 

data = {
    "department" : ["maths", "philosophy", "sales", "sales", "finance"],
    "employees" : ["Aisha", "Aliya", "Jay", "Ralph", "zigler"], 
    "salary" : [80000, 40000, 900000, 100000, 200000],
    "bonus" : [2000, 3000, 90000, 4000, 888]
}

df = pd.DataFrame(data)

# total compensation column
df["total_comp"] = df["salary"] + df["bonus"] #salaries and bonuses has been added successfully
print(df[["employees", "total_comp"]])

#finding the average 
avg_salary = df["salary"].mean()
print(avg_salary)

#finding average salary by department
dept_salary = df.groupby("department")["salary"].mean()
print(dept_salary)

#counting employee in each department
counting = df.groupby("department")["employees"].count()
print(counting)



