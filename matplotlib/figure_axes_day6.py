import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 140, 160]
students = [40, 35, 25, 10]
temperature = [28, 30, 31, 29]
departments = ["CSE", "ECE", "EEE", "MECH"]
marks = [40, 30, 20, 10]

axes[0, 0].plot(months, sales)
axes[0, 0].set_title("Sales")

axes[0, 1].plot(months, temperature)
axes[0, 1].set_title("Temperature")

axes[1, 0].bar(students, marks)
axes[1, 0].set_title("Student Marks")

axes[1, 1].hist(marks)
axes[1, 1].set_title("Marks Distribution")

plt.tight_layout()
plt.show()