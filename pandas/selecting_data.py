import pandas as pd

df = pd.read_csv("../datasets/students.csv")

print(df)

print(df["Name"])

print(type(df["Name"]))

print(df[["Name", "Marks"]])

print(type(df[["Name", "Marks"]]))

print(df.loc[0])

print(df.loc[0:2])

print(df.iloc[0])

print(df.iloc[0:2])

print(df.loc[0:3, ["Name", "Marks"]])

print(df.iloc[0:3, 1:3])

print(df.loc[2, "Name"])

print(df.iloc[2,1])

#captcha
students_df = pd.read_csv("../datasets/students.csv")
print(students_df["Department"])
print(students_df["Marks"])
print(students_df[["Name", "City"]])

print(students_df.loc[0:4])

print(students_df.iloc[0:5])


print(students_df.loc[2:6, ["Name", "Department", "Marks"]])

print(students_df.iloc[1:5, [1, 2, 3]])

print(students_df.loc[4, "Name"])

print(students_df.iloc[4, 1])