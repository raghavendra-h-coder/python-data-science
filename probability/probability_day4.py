#conditional probability

# 100 students
#
# 60 students → Pass
# 40 students → Fail
#
# 40 students have attendance >= 90
#
# 32 students passed

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students_with_statistics.csv"
)

high_attendance = students_df[
    students_df["Attendance"] >= 90
]

print(high_attendance)

probability_pass_given_attendance = (
    high_attendance["Result"]
    .eq("Pass")
    .mean()
)

print(
    probability_pass_given_attendance
)

table = pd.crosstab(
    students_df["Attendance"] >= 90,
    students_df["Result"]
)

print(table)

high_attendance = students_df[
    students_df["Attendance"] >= 90
]

print("High attendance students:")
print(high_attendance)


# Probability of Pass given high attendance

print(
    "\nP(Pass | Attendance >= 90):",
    probability_pass_given_attendance
)


# Contingency table

table = pd.crosstab(
    students_df["Attendance"] >= 90,
    students_df["Result"]
)
print("\nContingency Table:")
print(table)


