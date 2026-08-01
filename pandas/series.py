import pandas as pd
import numpy as np

marks = pd.Series([75, 80, 95])

print(marks)

print(marks.index)

# custom index
marks = pd.Series(
    [90, 95, 88],
    index=["Ram", "Sita", "Lakshman"]
)

print(marks)

print(marks.index)

print(marks["Ram"])

# Create Series from a Dictionary
student_marks = {
    "Ram": 90,
    "Sita": 95,
    "Krishna": 88
}

marks = pd.Series(student_marks)

print(marks)

# Create Series from a NumPy Array
arr = np.array([100, 200, 300])

series = pd.Series(arr)

print(series)


#captcha
ages = pd.Series([21, 25, 30, 28])

print(ages)
print(len(ages))
print(ages.values)
print(ages.index)

fruits = pd.Series([120, 60, 90], index=['Apple', 'Banana', 'Orange'])
print(fruits['Banana'])

sub_dict = {
    'Maths': 92,
    'Physics': 87,
    'Chemistry': 91
}

print(pd.Series(sub_dict))

print(pd.Series(np.array([5,10,15,20])))


#Arithmetic
s1 = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)

s2 = pd.Series(
    [1, 2, 3],
    index=["A", "B", "C"]
)

print(s1 + s2)
