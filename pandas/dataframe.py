import pandas as pd

students = {
    "Name": ["Ram", "Sita", "Krishna"],
    "Age": [21, 22, 20],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(students)

print(df)

print(df.shape)

print(df.columns)

print(df.index)

print(df.dtypes)

# shows the first rows, default it will show first 5 rows
print(df.head())

print(df.head(2))

# shows the last rows, default it will show last 5 rows
print(df.tail())

print(df.tail(2))

print(df.info())

print(df.describe())


#captcha
employees = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [75000, 60000, 82000, 70000]
}

employees_df = pd.DataFrame(employees)
print(employees_df)
print(employees_df.shape)
print(employees_df.columns)
print(employees_df.index)
print(employees_df.dtypes)

print(employees_df.head(2))
print(employees_df.tail(2))

print(employees_df.info())

print(employees_df.describe())


products = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [65000, 500, 1500],
    "Stock": [15, 100, 45]
}

df = pd.DataFrame(products)
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)