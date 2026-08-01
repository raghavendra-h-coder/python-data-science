import pandas as pd

students_df = pd.read_csv("../datasets/students.csv")

print(students_df)

print(students_df.groupby("Department").size())

print(students_df.groupby("Department")["Marks"].mean())

print(students_df.groupby("Department")["Marks"].max())

print(students_df.groupby("Department")["Marks"].min())

print(students_df.groupby("Department")["Marks"].sum())

print(students_df.groupby("Department")["Marks"].agg(
        ["count", "mean", "max", "min", "sum"]))

print(students_df.groupby("City")["Marks"].mean())

print(students_df.groupby(["Department", "City"])["Marks"].mean())

result = (
    students_df.groupby("Department")["Marks"]
               .mean()
               .reset_index()
)

print(result)


#captcha
students_df = pd.read_csv("../datasets/students.csv")

print(students_df)

print(students_df.groupby("City").size())

print(students_df.groupby("Department")["Marks"].mean())

print(students_df.groupby("Department")["Marks"].max())

print(students_df.groupby("City")["Age"].min())

print(students_df.groupby("Department")["Marks"].sum())

print(students_df.groupby("Department")["Marks"].agg(["count", "mean", "max", "min"]))

print(students_df.groupby(["Department", "City"])["Marks"].mean())

average_marks = students_df.groupby("Department")["Marks"].mean().reset_index()
print(average_marks)