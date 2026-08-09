import matplotlib.pyplot as plt
import pandas as pd

marks = [
    35, 42, 45, 51, 55,
    58, 62, 67, 72, 75,
    78, 82, 85, 91, 95
]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# student data set
students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students.csv"
)

plt.hist(
    students_df["Marks"],
    bins=10
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

plt.hist(students_df["Attendance"], bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.show()

plt.hist(students_df["Marks"], bins=[0, 40, 50, 60, 70, 80, 90, 100])
plt.title("Student Marks Range Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()