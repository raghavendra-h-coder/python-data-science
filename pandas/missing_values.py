import pandas as pd
import numpy as np

students = {
    "Name": ["Ram", "Sita", "Krishna", "Arjun"],
    "Age": [21, np.nan, 20, 22],
    "Marks": [85, 92, np.nan, 88]
}

df = pd.DataFrame(students)

print(df)

print(df.isnull().sum())

print(df.isnull().any())

print(df[df.isnull().any(axis=1)])

print(df.dropna())

print(df)

print(df.fillna(0))

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].median())

print(df)

df = pd.DataFrame(students)

print(df)

print(df.ffill())

print(df.bfill())


#captcha

employees = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, np.nan, 28, 30],
    "Salary": [50000, 60000, np.nan, 70000]
}

employees_df = pd.DataFrame(employees)
print(employees_df)

print(employees_df.isnull())

print(employees_df.isnull().sum())

print(employees_df.isnull().any(axis=1))

print(employees_df.dropna())

print(employees_df.fillna(0))

employees_df["Age"] = employees_df["Age"].fillna(employees_df["Age"].mean())
print(employees_df)

employees_df["Salary"] = employees_df["Salary"].fillna(employees_df["Salary"].median())
print(employees_df)

print(employees_df.ffill())
print(employees_df.bfill())

