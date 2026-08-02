import pandas as pd

employees = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "JoiningDate": [
        "2021-05-10",
        "2020-11-25",
        "2022-03-15",
        "2019-08-01"
    ]
}

employees_df = pd.DataFrame(employees)

print(employees_df)
print(employees_df.dtypes)

employees_df["JoiningDate"] = pd.to_datetime(
    employees_df["JoiningDate"]
)

print(employees_df.dtypes)

print(
    employees_df["JoiningDate"].dt.year
)

print(
    employees_df["JoiningDate"].dt.month
)

print(
    employees_df["JoiningDate"].dt.day
)

print(
    employees_df["JoiningDate"].dt.day_name()
)

print(pd.Timestamp.now())

today = pd.Timestamp.now()

employees_df["DaysWorked"] = (
    today - employees_df["JoiningDate"]
).dt.days

print(employees_df)

print(
    employees_df[
        employees_df["JoiningDate"].dt.year >= 2021
    ]
)

employees_df["ConfirmationDate"] = (
    employees_df["JoiningDate"] +
    pd.Timedelta(days=180)
)

print(employees_df)

employees_df["ReminderDate"] = (
    employees_df["JoiningDate"] -
    pd.Timedelta(days=30)
)

print(employees_df)


#captcha
students = {
    "Name": [
        "Ram",
        "Sita",
        "Lakshman",
        "Hanuman"
    ],
    "AdmissionDate": [
        "2023-06-15",
        "2022-08-20",
        "2021-01-10",
        "2024-02-01"
    ]
}

students_df = pd.DataFrame(students)

students_df["AdmissionDate"] = pd.to_datetime(students_df["AdmissionDate"])
print(students_df)

print(students_df["AdmissionDate"].dt.year)
print(students_df["AdmissionDate"].dt.month)
print(students_df["AdmissionDate"].dt.day)
print(students_df["AdmissionDate"].dt.day_name())

students_df["DaysSinceAdmission"] = (pd.Timestamp.now() - students_df["AdmissionDate"]).dt.days

print(students_df)

print(students_df[students_df["AdmissionDate"].dt.year >= 2022])

students_df["CourseCompletion"] = students_df["AdmissionDate"] + pd.Timedelta(days=365)
print(students_df)

students_df["ReminderDate"] = students_df["AdmissionDate"] - pd.Timedelta(days=15)
print(students_df)
