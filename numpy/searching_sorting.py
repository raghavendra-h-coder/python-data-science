import numpy as np

numbers = np.array([50, 10, 30, 20, 40])

print(np.sort(numbers))

# sorting in descending order
print(np.sort(numbers)[::-1])

matrix = np.array([
    [30, 10, 20],
    [90, 70, 80]
])

# sorting row wise
print(np.sort(matrix))

# sorting column wise
print(np.sort(matrix, axis=0))

# axis=0 → sort each column
# axis=1 → sort each row (default for 2D arrays)

arr = np.array([40, 10, 30, 20])

print(np.argsort(arr))

arr = np.array([10,20,10,30,20,40,40])

print(np.unique(arr))

marks = np.array([35,80,55,90,20])

print(np.where(marks > 50))

arr = np.array([0,1,2,0,3,4,0])

print(np.count_nonzero(arr))

marks = np.array([35,80,55,90,20])

print(np.count_nonzero(marks >= 40))


#real time example
salary = np.array([
    50000,
    70000,
    70000,
    90000,
    50000,
    120000
])

print("Unique Salaries:")
print(np.unique(salary))

print("Sorted:")
print(np.sort(salary))

print("Employees earning above 60000:")
print(np.where(salary > 60000))

print("Count above 60000:")
print(np.count_nonzero(salary > 60000))

#captcha
numbers = np.array([45,12,78,23,56,12,90])
print(np.sort(numbers))
print(np.sort(numbers)[::-1])
print(np.unique(numbers))

marks = np.array([35,78,91,42,67,91,35])

print(np.where(marks > 70))
print(np.count_nonzero(marks > 70))
print(np.unique(marks))

matrix = np.array([
    [9,3,6],
    [2,8,1]
])

print(np.sort(matrix))
print(np.sort(matrix, axis=0))


#np.searchsorted()
# np.searchsorted() is designed to work on a sorted array.
arr = np.array([10,2,30,4,50])

print(np.searchsorted(arr, 35))
