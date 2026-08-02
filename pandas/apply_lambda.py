import pandas as pd

students = {
    "Name": ["Ram", "Sita", "Lakshman", "Hanuman"],
    "Marks": [95, 82, 68, 90]
}

students_df = pd.DataFrame(students)

print(students_df)

students_df["UpdatedMarks"] = students_df["Marks"].apply(
    lambda x: x + 5
)

print(students_df)

students_df["Grade"] = students_df["Marks"].apply(
    lambda x: "A" if x >= 90
    else "B" if x >= 75
    else "C"
)

print(students_df)

def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    else:
        return "C"

students_df["Grade"] = students_df["Marks"].apply(grade)

print(students_df)

employees = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Basic": [50000, 60000, 70000],
    "Bonus": [5000, 6000, 7000]
}

employees_df = pd.DataFrame(employees)

employees_df["TotalSalary"] = employees_df.apply(
    lambda row: row["Basic"] + row["Bonus"],
    axis=1
)

print(employees_df)

employees_df["Tax"] = employees_df.apply(
    lambda row:
        row["TotalSalary"] * 0.10
        if row["TotalSalary"] > 60000
        else row["TotalSalary"] * 0.05,
    axis=1
)

print(employees_df)



#captcha
employees = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Salary": [45000, 75000, 62000, 90000]
}

employees_df = pd.DataFrame(employees)

employees_df["Bonus"] = employees_df.apply(
    lambda row: row["Salary"] * 0.10,
    axis=1
)
print(employees_df)

employees_df["Category"] = employees_df.apply(
    lambda row: 'High' if row["Salary"] >= 70000
    else 'Medium ' if row["Salary"] >= 50000 else 'Low',
    axis=1
)

print(employees_df)


employees = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Basic": [50000, 60000, 70000],
    "Allowance": [5000, 7000, 9000]
}

employees_df = pd.DataFrame(employees)

employees_df["TotalSalary"] = employees_df.apply(
    lambda row: row["Basic"] + row["Allowance"], axis=1
)

print(employees_df)

employees_df["Tax"] = employees_df.apply(
    lambda row: row["TotalSalary"] * 0.10 if row["TotalSalary"] > 70000 else row["TotalSalary"] * 0.05,
    axis=1
)

print(employees_df)