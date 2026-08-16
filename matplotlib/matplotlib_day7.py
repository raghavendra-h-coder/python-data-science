import matplotlib.pyplot as plt
import pandas as pd

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 120, 140, 160, 180]
sales_2026 = [110, 130, 150, 170, 200]

fig, ax = plt.subplots()

ax.plot(
    months,
    sales_2025,
    label="2025"
)

ax.plot(
    months,
    sales_2026,
    label="2026"
)

ax.set_title("Sales Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.legend()

ax.grid(axis="y")

plt.show()


months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 150, 180]

fig, ax = plt.subplots()

ax.tick_params(
    axis="x",
    rotation=45
)

plt.plot(months, sales)

ax.set_title("Monthly Sales")

ax.annotate(
    "Highest",
    xy=("Apr", 180)
)

ax.annotate(
    "Highest Sales",
    xy=("Apr", 180),
    xytext=("Feb", 160),
    arrowprops=dict(
        arrowstyle="->"
    )
)

plt.show()


#captcha
fig, ax = plt.subplots(
    figsize=(9, 6)
)

students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students.csv"
)

top_students = students_df.nlargest(
    5,
    "Marks"
)

bars = ax.bar(
    top_students["Name"],
    top_students["Marks"]
)

ax.set_title(
    "Top 5 Students by Marks"
)

ax.set_xlabel(
    "Student"
)

ax.set_ylabel(
    "Marks"
)

ax.grid(
    axis="y"
)

ax.tick_params(
    axis="x",
    rotation=30
)

for i, mark in enumerate(
    top_students["Marks"]
):

    ax.text(
        i,
        mark,
        str(mark),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    "top_students.png",
    dpi=300
)

plt.show()


# practice
months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 120, 140, 160, 180]
sales_2026 = [110, 130, 150, 170, 200]

fig, ax = plt.subplots()
ax.plot(
    months,
    sales_2025,
    label="sales_2025",
)

ax.plot(
    months,
    sales_2026,
    label="sales_2026",
)

ax.set_title("Sales Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.legend()
ax.grid(axis="y")
plt.show()


fig, ax = plt.subplots()

ax.scatter(students_df["Attendance"], students_df["Marks"])

ax.set_title("Attendance vs Marks")
ax.set_xlabel("Attendance")
ax.set_ylabel("Marks")

ax.axhline(40)

plt.show()


