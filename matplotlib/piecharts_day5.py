import matplotlib.pyplot as plt
import pandas as pd

departments = ["CSE", "ECE", "EEE"]
students = [40, 35, 25]

plt.pie(
    students,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90,
    explode=[0.1, 0, 0]
)

#making pie circular
plt.axis("equal")

plt.title("Students by Department")

plt.show()


#student dataset
students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students.csv"
)

department_count = students_df.groupby("Department").size()
print(department_count)

plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%"
)

plt.title("Students by Department")
plt.axis("equal")
plt.show()

# sub-plots
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 140, 160]

temperature = [28, 30, 31, 29]

plt.subplot(1, 2, 1)

plt.plot(months, sales)
plt.title("Sales")


plt.subplot(1, 2, 2)

plt.plot(months, temperature)
plt.title("Temperature")

# automatically adjusts spacing
plt.tight_layout()

plt.show()


# captcha
departments = ["CSE", "ECE", "EEE", "MECH"]
students = [40, 30, 20, 10]

plt.pie(
    students,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90,
)

plt.axis("equal")

plt.title("Students by Department")

plt.show()


plt.pie(
    students,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90,
    explode=[0.1, 0, 0, 0]
)

plt.axis("equal")

plt.title("Students by Department")

plt.show()


plt.subplot(2, 2, 1)
plt.hist(students_df["Marks"], bins=5)

plt.title("Students by Department")
plt.subplot(2, 2, 2)

plt.hist(students_df["Attendance"], bins=5)
plt.title("Students by Attendance")

plt.subplot(2, 2, 3)

plt.plot(students_df["Attendance"], students_df["Marks"], marker="o")
plt.title("Attendance by Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")

plt.subplot(2, 2, 4)
plt.pie(
    students,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90,
)


plt.axis("equal")
plt.title("Students by Department")

plt.tight_layout()
plt.show()
