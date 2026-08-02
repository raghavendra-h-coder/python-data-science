import pandas as pd

employees = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [75000, 60000, 82000, 70000]
}

employees_df = pd.DataFrame(employees)

print(employees_df)

employees_df.to_csv("employees.csv")

employees_df.to_csv(
    "employees_without_index.csv",
    index=False
)

new_df = pd.read_csv(
    "employees_without_index.csv"
)

print(new_df)

employees_df.to_excel(
    "employees.xlsx",
    index=False
)

excel_df = pd.read_excel(
    "employees.xlsx"
)

print(excel_df)

employees_df[
    ["Name", "Salary"]
].to_csv(
    "salary_report.csv",
    index=False
)

it_df = employees_df[
    employees_df["Department"] == "IT"
]

it_df.to_csv(
    "it_employees.csv",
    index=False
)

sorted_df = employees_df.sort_values(
    "Salary",
    ascending=False
)

sorted_df.to_excel(
    "highest_salary.xlsx",
    index=False
)



#captcha
students = {
    "Name": [
        "Ram",
        "Sita",
        "Lakshman",
        "Hanuman"
    ],
    "Department": [
        "CSE",
        "ECE",
        "EEE",
        "CSE"
    ],
    "Marks": [
        92,
        88,
        79,
        95
    ]
}

students_df = pd.DataFrame(students)

students_df.to_csv("students.csv")

students_df.to_csv("students_clean.csv", index=False)

students_df = pd.read_csv(
    "students_clean.csv"
)

print(students_df)

students_df = pd.DataFrame(students)

students_df.to_excel("students.xlsx")

students_df = pd.read_excel(
    "students.xlsx"
)

print(students_df)

students_df[["Name", "Marks"]].to_excel("marks_report.xlsx")

students_df = pd.DataFrame(students)

students_df[students_df["Department"] == "CSE"].to_csv("cse-students.csv")

students_df["Marks"].sort_values(ascending=False).to_excel("top_students.xlsx")

