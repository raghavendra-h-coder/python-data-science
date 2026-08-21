from statistics import median

import pandas as pd
import numpy as np

students_df = pd.read_csv("datasets/students.csv")

print(students_df)

print("\nShape:")
print(students_df.shape)

print("\nColumns:")
print(students_df.columns)

print("\nData Types:")
print(students_df.dtypes)

print("\nInformation:")
print(students_df.info())

print(students_df.head())

print(students_df.tail())

print(students_df.describe())

print(students_df.isnull().sum())

print(
    students_df[
        students_df.duplicated(
            subset=["Name", "Department", "Marks"],
            keep=False
        )
    ]
)

print(students_df[["Name", "Department", "Marks"]])

print(students_df[students_df['Marks'] > 90])

print(students_df[students_df['Department'] == 'CSE'])

# replace missing age with median
students_df["Age"] = students_df["Age"].fillna(students_df["Age"].median())

print(students_df)

# replace missing marks with median
students_df["Marks"] = students_df["Marks"].fillna(students_df["Marks"].median())

print(students_df)

# replace attendance with median
students_df["Attendance"] = students_df["Attendance"].fillna(students_df["Attendance"].median())

print(students_df)

# replace the city with mode
students_df["City"] = students_df["City"].fillna(students_df["City"].mode()[0])
print(students_df)

print(students_df.isnull().sum())

students_df = students_df.drop_duplicates()

print(students_df[students_df.duplicated()])

cleaned_students = students_df.copy()

cleaned_students.to_csv("reports/cleaned_students.csv", index=False)

# converting string to date time
students_df["AdmissionDate"] = pd.to_datetime(students_df["AdmissionDate"])
print(students_df)

# add new column as Grade
students_df["Grade"] = students_df["Marks"].apply(
    lambda x: 'A' if x >= 90
    else 'B' if x >= 80
    else 'C' if x >= 70
    else 'D'
)

print(students_df)

students_df["Result"] = students_df["Marks"].apply(
    lambda marks: 'Pass' if marks >= 40
    else 'Fail'
)

print(students_df)

students_df["AttendanceStatus"] = students_df["Attendance"].apply(
    lambda attendance: 'Excellent' if attendance >= 90
    else 'Good' if attendance >= 75
    else 'Low'
)

print(students_df)

students_df.to_csv(
    "datasets/students_with_statistics.csv",
    index=False
)

#statistics
#marks statistics

print(students_df["Marks"].sum())
print(students_df["Marks"].mean())
print(students_df["Marks"].median())
print(students_df["Marks"].max())
print(students_df["Marks"].min())
print(students_df["Marks"].std())
print(students_df["Marks"].var())

# finding top scoring n students
print(students_df["Marks"].nlargest(5))

#find students above 90 marks
high_scorers = students_df[students_df["Marks"] > 90]
print(high_scorers)

#department wise students count
print(students_df.groupby("Department").size())

# average marks by department
department_average = students_df.groupby("Department")["Marks"].mean()
print(department_average)

#maximum marks by department
print(students_df.groupby("Department")["Marks"].max())

#minimum marks by department
print(students_df.groupby("Department")["Marks"].min())

#aggregation by department
print(students_df.groupby("Department")["Marks"].agg([
    'sum', 'mean', 'median', 'max', 'min', 'std', 'var'
]))


#city wise analysis
#number of students from each city
print(students_df.groupby('City').size())

#average marks by city
print(students_df.groupby('City')['Marks'].mean())



#Attendance analysis
#attendance average by department
print(students_df.groupby('Department')['Attendance'].mean())

#high performers= high marks + high attendance
high_performers = students_df[(students_df["Marks"] >= 85) & (students_df["Attendance"] >= 90)]
print(high_performers)

high_performers.to_csv("reports/high_performers.csv", index=False)

#top students
top_students = students_df.nlargest(5, ["Marks"])
top_students = top_students[
[
        "Name",
        "Department",
        "Marks",
        "Attendance",
        "Grade"
    ]
]
print(top_students)

top_students.to_csv("reports/top_students.csv", index=False)

print(students_df['Grade'].value_counts())

grade_report = (
    students_df["Grade"]
    .value_counts()
    .rename_axis("Grade")
    .reset_index(name="StudentCount")
)

grade_report.to_csv("reports/grade_report.csv", index=False)

print(students_df['Result'].value_counts())

result_report = (
    students_df["Result"]
    .value_counts()
    .rename_axis("Result")
    .reset_index(name="StudentCount")
)

result_report.to_csv("reports/result_report.csv", index=False)

print(students_df.groupby("Department")["Marks"].max().idxmax())


# preparing department wise report
department_report = (
    students_df
    .groupby("Department")
    .agg(
        StudentCount=("StudentID", "count"),
        AverageMarks=("Marks", "mean"),
        HighestMarks=("Marks", "max"),
        LowestMarks=("Marks", "min"),
        AverageAttendance=("Attendance", "mean")
    )
    .reset_index()
)

department_report = department_report.sort_values(
    "AverageMarks",
    ascending=False
)

department_report.to_csv(
    "reports/department_performance.csv",
    index=False
)

# city wise report
city_report = (
    students_df
    .groupby("City")
    .agg(
        StudentCount=("StudentID", "count"),
        AverageMarks=("Marks", "mean"),
        HighestMarks=("Marks", "max"),
        AverageAttendance=("Attendance", "mean")
    )
    .reset_index()
)

city_report = city_report.sort_values(
    "AverageMarks",
    ascending=False
)

city_report.to_csv("reports/city_performance.csv", index=False)


# exporting to excel
with pd.ExcelWriter(
    "reports/student_performance_report.xlsx"
) as writer:

    cleaned_students.to_excel(
        writer,
        sheet_name="Students",
        index=False
    )

    department_report.to_excel(
        writer,
        sheet_name="Departments",
        index=False
    )

    city_report.to_excel(
        writer,
        sheet_name="Cities",
        index=False
    )

    top_students.to_excel(
        writer,
        sheet_name="Top Students",
        index=False
    )

    high_performers.to_excel(
        writer,
        sheet_name="High Performers",
        index=False
    )

    grade_report.to_excel(
        writer,
        sheet_name="Grades",
        index=False
    )

    result_report.to_excel(
        writer,
        sheet_name="Results",
        index=False
    )