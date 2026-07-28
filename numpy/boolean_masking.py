import numpy as np

marks = np.array([35, 42, 55, 68, 89, 91, 25])

print(marks)

# Suppose you want only students who passed (marks ≥ 40).

print(marks >=40)
print(marks[marks >= 40])

print((marks >= 50) & (marks <= 90))
print(marks[(marks >= 50) & (marks <= 90)])

print(marks[(marks < 40) | (marks > 90)])

print(marks[~(marks >= 40)])


#captcha
ages = np.array([12,18,22,35,45,60,75])

print(ages[ages >= 18])

print(ages[ages < 40])

print(ages[(ages >= 20) & (ages <= 60)])


temperature = np.array([28,31,35,39,41,26,30])

print(temperature[temperature > 35])

print(temperature[temperature <= 30])

print(temperature[(temperature >= 30) & (temperature <= 40)])


prices = np.array([100,250,500,750,1000,1500])

print(prices[prices > 500])

print(prices[~(prices == 750)])

print(prices[(prices > 1000) | (prices < 300)])