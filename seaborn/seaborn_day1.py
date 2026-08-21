import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students_with_statistics.csv"
)

# marks
sns.set_theme(style="whitegrid")

sns.histplot(
    data=students_df,
    x="Marks"
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# attendance
sns.histplot(
    data=students_df,
    x="Attendance",
    kde=True
)

plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")

plt.show()

# Marks by Department
sns.histplot(
    data=students_df,
    x="Marks",
    hue="Department",
    bins=10,
    kde=True
)

plt.title("Marks Distribution by Department")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# barplot
fig, ax = plt.subplots()

sns.barplot(
    data=students_df,
    x="Department",
    y="Marks",
    estimator="median", # by default barplot uses mean as estimator
    ax=ax
)

ax.set_title("Average Marks by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Marks")

plt.show()


# barplot with hue
fig, ax = plt.subplots()
sns.barplot(
    data=students_df,
    x="Department",
    y="Marks",
    hue="Grade",
    ax=ax
)

ax.set_title("Marks by Department and Grade")
ax.set_xlabel("Department")
ax.set_ylabel("Marks")

plt.show()

# countplot
fig, ax = plt.subplots()

sns.countplot(
    data=students_df,
    x="Department",
    ax=ax
)

ax.set_title("Number of Students by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Students")

plt.show()

# horizontal countplot
fig, ax = plt.subplots()

sns.countplot(
    data=students_df,
    y="Department",
    ax=ax
)

ax.set_title("Students by Department")

plt.show()


# sorting
department_order = (
    students_df
    .groupby("Department")["Marks"]
    .mean()
    .sort_values()
    .index
)

print(department_order)

fig, ax = plt.subplots()

sns.barplot(
    data=students_df,
    x="Department",
    y="Marks",
    order=department_order,
    ax=ax
)

ax.set_title("Departments by Average Marks")

plt.show()


# adding values to bars
fig, ax = plt.subplots()

sns.barplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

for container in ax.containers:
    ax.bar_label(container, fmt="%.1f")

ax.set_title("Average Marks by Department")

plt.show()

# number of students by grade
fig, ax = plt.subplots()
sns.countplot(
    data=students_df,
    x="Grade",
    ax=ax
)

ax.set_title("Grades by Students")
ax.set_xlabel("Grade")
ax.set_ylabel("Number of Students")

plt.show()


# boxplot
fig, ax = plt.subplots()

sns.boxplot(
    data=students_df,
    y="Marks",
    ax=ax
)

ax.set_title("Distribution of Student Marks")
ax.set_ylabel("Marks")

plt.show()

# marks by department
fig, ax = plt.subplots()

sns.boxplot(
    data=students_df,
    x='Department',
    y="Marks",
    ax=ax
)

ax.set_title("Distribution of Student Marks")
ax.set_xlabel("Department")
ax.set_ylabel("Marks")

plt.show()

# marks by grade
fig, ax = plt.subplots()

sns.boxplot(
    data=students_df,
    x='Marks',
    y="Grade",
    ax=ax
)

ax.set_title("Marks by Grade")
ax.set_xlabel("Marks")
ax.set_ylabel("Grade")

plt.show()

#attendance distribution by department
fig, ax = plt.subplots()

sns.boxplot(
    data=students_df,
    x='Department',
    y="Attendance",
    ax=ax
)

ax.set_title("Attendance distribution by department")
ax.set_xlabel("Department")
ax.set_ylabel("Attendance")

plt.show()


# boxplot + swarmplot
fig, ax = plt.subplots()

sns.boxplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

sns.swarmplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

ax.set_title("Marks Distribution by Department")

plt.show()


# violinplot

fig, ax = plt.subplots()

sns.violinplot(
    data=students_df,
    y="Marks",
    ax=ax
)

ax.set_title("Distribution of Student Marks")
ax.set_ylabel("Marks")

plt.show()

# marks by department
fig, ax = plt.subplots()

sns.violinplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

ax.set_title("Marks Distribution by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Marks")

plt.show()


# violin vs boxplot
fig, ax = plt.subplots()

sns.violinplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

sns.boxplot(
    data=students_df,
    x="Department",
    y="Marks",
    width=0.15,
    ax=ax
)

ax.set_title("Marks Distribution by Department")

plt.show()


# violinplot with hue
fig, ax = plt.subplots()

sns.violinplot(
    data=students_df,
    x="Department",
    y="Marks",
    hue="Grade",
    ax=ax
)

ax.set_title("Marks by Department and Grade")

plt.show()


# heatmap
correlation = students_df.corr(numeric_only=True)

fig, ax = plt.subplots()

sns.heatmap(
    correlation,
    annot=True,
    ax=ax
)

ax.set_title("Correlation Matrix")

plt.show()


# pairplot
sns.pairplot(
    students_df[
        ["Age", "Marks", "Attendance"]
    ],
    kind="reg"
)

plt.show()


# regplot
fig, ax = plt.subplots()

sns.regplot(
    data=students_df,
    x="Attendance",
    y="Marks",
    ax=ax
)

ax.set_title("Attendance vs Marks")
ax.set_xlabel("Attendance")
ax.set_ylabel("Marks")

plt.show()


# Age vs marks
fig, ax = plt.subplots()

sns.regplot(
    data=students_df,
    x="Age",
    y="Marks",
    ax=ax
)

ax.set_title("Age vs Marks")
ax.set_xlabel("Age")
ax.set_ylabel("Marks")

plt.show()

#hue
fig, ax = plt.subplots()

sns.lmplot(
    data=students_df,
    x="Attendance",
    y="Marks",
    hue="Result"
)

ax.set_title("Attendance vs Marks")
ax.set_xlabel("Attendance")
ax.set_ylabel("Marks")

plt.show()