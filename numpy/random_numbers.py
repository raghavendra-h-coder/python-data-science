import numpy as np

# Generate random numbers between 0 and 1.
print(np.random.rand())

# generates 5 random numbers between 0 to 1
print(np.random.rand(5))

# generates random matrix with 2 rows and 3 columsn with values between 0 and 1
print(np.random.rand(2,3))

# 1 ≤ number < 10
# Notice that 10 is excluded.
print(np.random.randint(1,10))

#generates 5 integers from 1 to 9
print(np.random.randint(1,10,5))

#generates matrix with 3 rows and 4 columns with values between 1 to 99
print(np.random.randint(1,100,(3,4)))

fruits = np.array([
    "Apple",
    "Banana",
    "Orange",
    "Mango"
])

#chooses only one
print(np.random.choice(fruits))

#chooses 3 values
print(np.random.choice(fruits, 3))

numbers = np.array([1,2,3,4,5])

#shuffle modifies the original array
np.random.shuffle(numbers)

print(numbers)


#captcha
print(np.random.rand())
print(np.random.rand(5))
print(np.random.rand(3,3))

print(np.random.randint(10,50))
print(np.random.randint(100,200,10))
print(np.random.randint(1, 10, (2,4)))

colors = np.array([
    "Red",
    "Green",
    "Blue",
    "Black",
    "White"
])

print(np.random.choice(colors))
print(np.random.choice(colors, 3))

numbers = np.array([10,20,30,40,50])

np.random.shuffle(numbers)
print(numbers)

np.random.seed(100)
print(np.random.randint(1,20,5))
print(np.random.randint(1,20,5))