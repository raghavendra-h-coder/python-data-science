import matplotlib.pyplot as plt
import pandas as pd

# positive relationship
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 55, 65, 72, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

#negative relationship
price = [10, 20, 30, 40, 50]
demand = [95, 85, 70, 55, 40]

plt.scatter(price, demand)

plt.title("Price vs Demand")
plt.xlabel("Price")
plt.ylabel("Demand")
plt.show()

# student data set
students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students.csv"
)

plt.scatter(
    students_df["Attendance"],
    students_df["Marks"],
    alpha=0.6,
    s=80
)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

#age vs marks
plt.scatter(students_df["Age"], students_df["Marks"])

plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()


#captcha
hours = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 45, 52, 60, 68, 78, 88]

plt.scatter(hours, marks)
plt.title("Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()