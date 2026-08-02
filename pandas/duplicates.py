import pandas as pd

students = {
    "Name": ["Ram", "Sita", "Ram", "Lakshman", "Sita"],
    "Marks": [90, 95, 90, 88, 95],
    "City": ["Hyderabad", "Delhi", "Hyderabad", "Chennai", "Delhi"]
}

students_df = pd.DataFrame(students)

print(students_df)

print(students_df.duplicated())

# display duplicates
print(students_df[students_df.duplicated()])

# drop duplicates
result = students_df.drop_duplicates()

print(result)

#keep first duplicate
print(students_df.drop_duplicates(keep="first"))

# keep last duplicate
print(students_df.drop_duplicates(keep="last"))

#remove all duplicates
print(
    students_df.drop_duplicates(
        keep=False
    )
)

# check duplicates based on column
print(
    students_df.duplicated(
        subset=["Name"]
    )
)

#remove duplicates in the column 'Name'
print(
    students_df.drop_duplicates(
        subset=["Name"]
    )
)

#captcha
employees = {
    "EmpID": [101,102,103,102,104,101],
    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Priya",
        "Sneha",
        "Rahul"
    ],
    "Department": [
        "IT",
        "HR",
        "Finance",
        "HR",
        "IT",
        "IT"
    ]
}

employees_df = pd.DataFrame(employees)

print(employees_df)

print(employees_df.duplicated())

print(employees_df[employees_df.duplicated()])

print(
    employees_df.drop_duplicates()
)

print(employees_df.drop_duplicates(keep="last"))

print(employees_df.drop_duplicates(keep=False))

print(employees_df.duplicated(subset=["EmpID"]))

print(employees_df.drop_duplicates(subset=["EmpID"]))

