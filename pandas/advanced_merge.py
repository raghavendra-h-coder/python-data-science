import pandas as pd

employees = {
    "EmpID": [101, 102, 103],
    "Name": ["Rahul", "Priya", "Amit"],
    "DeptID": [1, 2, 1]
}

departments = {
    "DepartmentID": [1, 2],
    "Department": ["IT", "HR"]
}

employees_df = pd.DataFrame(employees)
departments_df = pd.DataFrame(departments)

result = pd.merge(
    employees_df,
    departments_df,
    left_on="DeptID",
    right_on="DepartmentID"
)

print(result)

# Removing the Extra Column
result = result.drop(columns=["DepartmentID"])

print(result)

# Duplicate Column Names(suffixes)
students = {
    "StudentID": [1, 2],
    "Name": ["Ram", "Sita"],
    "City": ["Hyderabad", "Delhi"]
}

hostels = {
    "StudentID": [1, 2],
    "City": ["Pune", "Mumbai"],
    "Hostel": ["A", "B"]
}

students_df = pd.DataFrame(students)
hostels_df = pd.DataFrame(hostels)

result = pd.merge(
    students_df,
    hostels_df,
    on="StudentID"
)

print(result)

# Instead of _x and _y:
# custom suffixes

result = pd.merge(
    students_df,
    hostels_df,
    on="StudentID",
    suffixes=("_Home", "_Hostel")
)

print(result)

batch1 = pd.DataFrame({
    "Name": ["Ram", "Sita"]
})

batch2 = pd.DataFrame({
    "Name": ["Lakshman", "Hanuman"]
})

result = pd.concat([batch1, batch2])

print(result)

# reset index
result = pd.concat(
    [batch1, batch2],
    ignore_index=True
)

print(result)

# Horizontal concat
names = pd.DataFrame({
    "Name": ["Ram", "Sita"]
})

marks = pd.DataFrame({
    "Marks": [95, 99]
})

result = pd.concat(
    [names, marks],
    axis=1
)

print(result)


#captcha

students = {
    "StudentID": [1,2,3],
    "Name": ["Ram","Sita","Lakshman"],
    "CourseID": [101,102,103]
}

courses = {
    "ID": [101,102,103],
    "Course": ["Python","Pandas","Machine Learning"]
}

students_df = pd.DataFrame(students)
courses_df = pd.DataFrame(courses)

result = pd.merge(
    students_df,
    courses_df,
    left_on="CourseID",
    right_on="ID"
)

print(result)

print(result.drop(columns=["ID"]))

semester1 = pd.DataFrame({
    "Student": ["Ram","Sita"]
})

semester2 = pd.DataFrame({
    "Student": ["Lakshman","Hanuman"]
})

print(pd.concat([semester1, semester2]))

print(pd.concat([semester1, semester2], ignore_index=True))

names = pd.DataFrame({
    "Name": ["Ram","Sita"]
})

marks = pd.DataFrame({
    "Marks": [90,95]
})

result = pd.concat(
    [names, marks],
    axis=1
)

print(result)