import pandas as pd

employees = {
    "EmpID": [101, 102, 103, 104],
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "DeptID": [1, 2, 1, 3]
}

departments = {
    "DeptID": [1, 2, 3],
    "Department": ["IT", "HR", "Finance"]
}

employees_df = pd.DataFrame(employees)
departments_df = pd.DataFrame(departments)

print(employees_df)
print()
print(departments_df)

result = pd.merge(
    employees_df,
    departments_df,
    on="DeptID"
)

print(result)

employees = {
    "EmpID": [101,102,103,104,105],
    "Name": ["Rahul","Priya","Amit","Sneha","Kiran"],
    "DeptID": [1,2,1,3,4]
}

employees_df = pd.DataFrame(employees)

result = pd.merge(
    employees_df,
    departments_df,
    on="DeptID",
    how="left"
)

print(result)

result = pd.merge(
    employees_df,
    departments_df,
    on="DeptID",
    how="right"
)

print(result)

result = pd.merge(
    employees_df,
    departments_df,
    on="DeptID",
    how="outer"
)

print(result)


#captcha
students = {
    "StudentID": [1,2,3,4],
    "Name": ["Ram","Sita","Lakshman","Hanuman"],
    "CourseID": [101,102,101,103]
}

courses = {
    "CourseID": [101,102,103],
    "CourseName": [
        "Python",
        "Data Science",
        "Machine Learning"
    ]
}

students_df = pd.DataFrame(students)
courses_df = pd.DataFrame(courses)

print(students_df)
print(courses_df)

result = pd.merge(
    students_df,
    courses_df,
on="CourseID")

print(result)

students = {
    "StudentID": [1,2,3,4,5],
    "Name": ["Ram","Sita","Lakshman","Hanuman","Bharat"],
    "CourseID": [101,102,101,103,104]
}

students_df = pd.DataFrame(students)

print(students_df)

result = pd.merge(
    students_df,
    courses_df,
    on="CourseID",
    how="left"
)

print(result)

result = pd.merge(
    students_df,
    courses_df,
    on="CourseID",
    how="right"
)

print(result)

result = pd.merge(
    students_df,
    courses_df,
    on="CourseID",
    how="outer"
)

print(result)