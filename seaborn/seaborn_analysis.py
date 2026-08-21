import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


students_df = pd.read_csv(
    "../student_performance_analysis/datasets/students_with_statistics.csv"
)

print(students_df)

#dataset overview
print(students_df.shape)
print(students_df.columns)
print(students_df.dtypes)
print(students_df.isnull().sum())
print(students_df.duplicated().sum())

# marks distribution
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(
    data=students_df,
    x="Marks",
    bins=10,
    kde=True,
    ax=ax
)

plt.title("Histogram of Students Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# attendance distribution
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(
    data=students_df,
    x="Attendance",
    bins=10,
    kde=True,
    ax=ax
)

plt.title("Histogram of Students Attendance")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# students by department
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(
    data=students_df,
    x="Department",
    ax=ax
)

ax.set_title("Number of Students by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Students")

plt.tight_layout()
plt.show()


# Average marks by department
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=students_df,
    x="Department",
    y="Marks",
    estimator="mean",
    ax=ax
)

ax.set_title("Average marks by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Marks")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.1f"
    )

plt.tight_layout()
plt.show()


# Marks distribution by department

fig, ax = plt.subplots(figsize=(10, 6))

sns.boxplot(
    data=students_df,
    x="Department",
    y="Marks",
    ax=ax
)

ax.set_title("Boxplot of Marks by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Marks")

plt.tight_layout()
plt.show()

# Attendance distribution by department
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(
    data=students_df,
    x="Department",
    y="Attendance",
    ax=ax
)

ax.set_title("Attendance distribution by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Attendance")
plt.tight_layout()
plt.show()

# Attendance vs Marks
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=students_df,
    x="Attendance",
    y="Marks",
    ax=ax
)

ax.set_title("Attendance vs Marks")
ax.set_xlabel("Attendance")
ax.set_ylabel("Marks")
plt.tight_layout()
plt.show()

# regression analysis for Attendance and Marks
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(
    data=students_df,
    x="Attendance",
    y="Marks",
    ax=ax
)

ax.set_title("Attendance vs Marks")
ax.set_xlabel("Attendance")
ax.set_ylabel("Marks")
plt.tight_layout()
plt.show()

# heatmap
correlation_matrix = students_df.corr(
    numeric_only=True
)

fig, ax = plt.subplots(
    figsize=(8, 6)
)

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Student Performance Correlation Matrix")

plt.tight_layout()
plt.show()

# pairplot
sns.pairplot(
    students_df[
        [
            "Age",
            "Marks",
            "Attendance",
            "Result"
        ]
    ],
    hue="Result",
    corner=True
)

plt.show()

# EDA Conclusions
print("\n===== EDA CONCLUSIONS =====")

print("""
1. Marks Distribution:
   4 students scored 90 marks and 1 student scored 95 ish marks; 2 students scored below 70 marks 

2. Attendance Distribution:
   overall 6 students have 90+ attendance; 1 student have above 95 attendance

3. Department Performance:
   CSE department has the highest average marks, while IT department has the lowest average marks

4. Attendance vs Marks:
   seems mostly as higher the attendance, higher the marks, but one outlier, even though attendance is good, but marks are average

5. Correlation:
   Attendance-> marks have a strong positive correlation, marks->age and age->attendance have medium correlation

6. Outliers:
   attendance vs marks, i observed one outlier and for CSE department out of the average percentile interval, there are 2 outliers observed
""")