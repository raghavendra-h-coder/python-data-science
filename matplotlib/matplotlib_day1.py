import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y,
    linestyle="--",
    marker="o")

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

plt.show()

# plot student marks
students_df = pd.read_csv("../datasets/students.csv")
print(students_df)

plt.plot(students_df["Name"], students_df["Marks"], marker="o")

plt.title("Students Marks")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.grid()

plt.show()

#captcha
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 140, 180, 200, 220]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

plt.show()

# temperature report
temperature = [28, 30, 32, 31, 29, 27, 26]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.plot(days, temperature, marker="o")

plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid()

plt.show()