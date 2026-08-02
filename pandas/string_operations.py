import pandas as pd

students = {
    "Name": [
        " Ram ",
        "SITA",
        "lakshman",
        "Hanuman"
    ],
    "City": [
        "Hyderabad",
        "DELHI",
        "chennai",
        " Pune "
    ]
}

students_df = pd.DataFrame(students)

print(students_df)

# uppercase
students_df["Name"] = students_df["Name"].str.upper()

print(students_df)

# lowercase
students_df["City"] = students_df["City"].str.lower()

print(students_df)

# title
students_df["City"] = students_df["City"].str.title()

# Remove Leading & Trailing Spaces
students_df["Name"] = students_df["Name"].str.strip()

students_df["City"] = students_df["City"].str.strip()

print(students_df)

print(students_df)

# Replace Text
students_df["City"] = students_df["City"].str.replace(
    "Delhi",
    "New Delhi"
)

print(students_df)

print(
    students_df["City"].str.contains("Hy")
)

print(
    students_df["Name"].str.startswith("R")
)

print(
    students_df["City"].str.endswith("i")
)

print(
    students_df["Name"].str.len()
)

employees = {
    "FullName": [
        "Rahul Sharma",
        "Priya Singh",
        "Amit Kumar"
    ]
}

employees_df = pd.DataFrame(employees)

employees_df[
    ["FirstName", "LastName"]
] = employees_df["FullName"].str.split(
    " ",
    expand=True
)

print(employees_df)



#captcha
employees = {
    "Name": [
        " rahul ",
        "PRIYA",
        "amit",
        " Sneha "
    ],
    "Email": [
        "Rahul@gmail.com",
        "PRIYA@GMAIL.COM",
        "amit@gmail.com",
        "Sneha@gmail.com"
    ]
}

employees_df = pd.DataFrame(employees)

print(employees_df)

employees_df["Name"] = employees_df["Name"].str.strip()
print(employees_df)

employees_df["Name"] = employees_df["Name"].str.title()
print(employees_df)

employees_df["Email"] = employees_df["Email"].str.lower()
print(employees_df)

employees_df["Email"] = employees_df["Email"].str.replace("gmail", "company")
print(employees_df)

print(employees_df["Email"].str.contains("company"))

print(employees_df["Name"].str.len())

full_names = pd.DataFrame({
    "FullName": [
        "Virat Kohli",
        "Rohit Sharma",
        "Jasprit Bumrah"
    ]
})

full_names[
    ["FirstName", "LastName"]
] = full_names["FullName"].str.split(
    " ",
    expand=True
)

print(full_names)