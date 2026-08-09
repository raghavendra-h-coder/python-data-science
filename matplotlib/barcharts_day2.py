import matplotlib.pyplot as plt
import pandas as pd

students = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [90, 80, 85, 95]

plt.bar(students, marks, width=0.6)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.grid(axis="y")

for i, mark in enumerate(marks):
    plt.text(
        i,
        mark,
        str(mark),
        ha="center",
        va="bottom"
    )

plt.show()

students_df = pd.read_csv("../student_performance_analysis/datasets/students.csv")

top_students = students_df.nlargest(
    5,
    "Marks"
)

plt.bar(
    top_students["Name"],
    top_students["Marks"]
)

plt.title("Top 5 Students")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.grid(axis="y")

plt.show()

# department average

department_average = students_df.groupby("Department")["Marks"].mean()
plt.bar(
    department_average.index,
    department_average.values
)

plt.title("Department Average")
plt.xlabel("Department")
plt.ylabel("Average")

plt.grid(axis="y")

plt.show()

#horizontal department chart

plt.barh(department_average.index, department_average.values)
plt.title("horizontal Department Average")
plt.xlabel("Department")
plt.ylabel("Average")
plt.grid(axis="y")
plt.show()


#captcha

students = ["Rahul", "Priya", "Amit", "Sneha", "Vijay"]
marks = [85, 92, 78, 95, 88]

plt.bar(
    students,
    marks,
)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

plt.barh(students, marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.grid(axis="y")

for i, mark in enumerate(marks):
    plt.text(i, mark, str(mark), ha="center", va="bottom")

plt.show()


city_report = students_df.groupby("City").size()
plt.bar(
    city_report.index,
    city_report.values
)

plt.title("City Report")
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.grid(axis="y")
plt.show()