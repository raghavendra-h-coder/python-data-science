#Scalar Broadcasting
import numpy as np

arr = np.array([10, 20, 30])

print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 10)

#Broadcasting with a 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix + 10)

#Row wise broadcasting
row = np.array([10, 20, 30])

print(matrix + row)

#column wise broadcasting
column = np.array([
    [10],
    [20]
])

print(matrix + column)

#captcha
marks = np.array([70, 80, 90, 100])
print(marks + 5)

employee_salary = np.array([
    [50000, 52000, 55000],
    [60000, 62000, 65000]
])

employee_salary = employee_salary + 2000
print(employee_salary)

bonus = np.array([1000, 2000, 3000])

employee_salary = employee_salary + bonus
print(employee_salary)

increment = np.array([
    [1000],
    [2000]
])

employee_salary = employee_salary + increment
print(employee_salary)