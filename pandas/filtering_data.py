import pandas as pd

df = pd.read_csv("../datasets/students.csv")

print(df)

print(df[df["Marks"] > 90])

print(df[df["Department"] == "CSE"])

print(df[df["City"] != "Chennai"])

print(df[df["Marks"] >= 85])

print(df[df["Age"] < 22])

print(
    df[
        (df["Department"] == "CSE") &
        (df["Marks"] > 80)
    ]
)

print(
    df[
        (df["City"] == "Hyderabad") |
        (df["City"] == "Bangalore")
    ]
)

print(
    df[
        df["City"].isin(
            ["Hyderabad", "Bangalore"]
        )
    ]
)

print(
    df[
        df["Marks"].between(80, 90)
    ]
)

print(
    df[
        ~df["Department"].isin(["IT"])
    ]
)


#capctha
students_df = pd.read_csv("../datasets/students.csv")

print(students_df[students_df["Marks"] > 85])

print(students_df[students_df["City"] == "Hyderabad"])

print(students_df[students_df["Department"] == "ECE"])

print(students_df[students_df["Age"] >= 22])

print(students_df[
          (students_df["Department"] == "CSE") &
          (students_df["Marks"] > 80)
      ])

print(students_df[
          (students_df["City"] == "Chennai") |
          (students_df["City"] == "Pune")
      ])

print(students_df[students_df["City"].isin(["Delhi", "Mumbai", "Hyderabad"])])

print(students_df[students_df["Marks"].between(80, 90)])

print(students_df[~students_df["City"].isin(["Bangalore"])])