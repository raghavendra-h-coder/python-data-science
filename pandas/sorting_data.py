import pandas as pd

df = pd.read_csv("../datasets/students.csv")

print(df)

print(df.sort_values("Marks"))

print(df.sort_values("Marks", ascending=False))

print(df.sort_values("Age"))

print(
    df.sort_values(
        ["Department", "Marks"],
        ascending=[True, False]
    )
)

print(df.sort_index())

print(df.sort_index(ascending=False))

print(
    df.nlargest(3, "Marks")
)

print(
    df.nsmallest(3, "Marks")
)

sorted_df = df.sort_values("Marks", ascending=False)

print(sorted_df)

sorted_df = sorted_df.reset_index(drop=True)

print(sorted_df)

# to modify the existing dataframe to be sorted itself, we use inplace=True
df.sort_values(
    "Marks",
    inplace=True
)


#captcha

students_df = pd.read_csv("../datasets/students.csv")

print(students_df.sort_values("Marks"))
print(students_df.sort_values("Marks", ascending=False))
print(students_df.sort_values("Age"))
print(students_df.sort_values([ "Department", "Marks"], ascending=[False, False]))

print(students_df.nlargest(5, "Marks"))
print(students_df.nsmallest(3, "Marks"))

sorted_students_df = students_df.sort_values("Marks", ascending=False)
print(sorted_students_df)
sorted_students_df = students_df.reset_index(drop=True)
print(sorted_students_df)