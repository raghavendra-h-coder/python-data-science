import numpy as np
import pandas as pd

marks = np.array([60, 70, 70, 80, 90])

print("Marks:", marks)

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))

marks_series = pd.Series(marks)
print(marks_series)

print("Mode:")
print(marks_series.mode())

# ddof = 0 means population; 1 means sample
print("sample variance:")
print(np.std(marks, ddof=1))

marks = np.array([
    10, 20, 30, 40,
    50, 60, 70, 80
])

q1 = np.percentile(marks, 25)
q2 = np.percentile(marks, 50)
q3 = np.percentile(marks, 75)

iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = marks[
    (marks < lower_bound) |
    (marks > upper_bound)
]

print("Outliers:", outliers)