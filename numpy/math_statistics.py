import numpy as np

marks = np.array([75, 82, 91, 68, 89])

print(marks)

print(np.sum(marks))

print(np.mean(marks))

print(np.median(marks))

print(np.min(marks))

print(np.min(marks))

print(np.argmin(marks))

print(np.argmax(marks))

print(np.std(marks))

print(np.var(marks))

print(np.cumsum(marks))

numbers = np.array([1,2,3,4])

print(np.cumprod(numbers))

marks = np.array([50,60,70,80,90])

print(np.percentile(marks, 50))

print(np.percentile(marks, 75))



#captcha
marks = np.array([65,72,81,90,95,88])
print(np.sum(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.min(marks))
print(np.max(marks))
print(np.argmax(marks))
print(np.argmin(marks))

sales = np.array([120,150,180,170,200])

print(np.std(sales))
print(np.var(sales))
print(np.cumsum(sales))

ages = np.array([18,22,25,30,35,40,45])

print(np.percentile(ages, 25))
print(np.percentile(ages, 50))
print(np.percentile(ages, 75))


#np.clip
import numpy as np

marks = np.array([-10, 25, 60, 105, 95])

print(np.clip(marks, 0, 100))

# Anything below 0 becomes 0, and anything above 100 becomes 100.
