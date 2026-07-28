import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr)

print(arr[0, 0])

print(arr[2, 1])

print(arr[0])

print(arr[2, :])

print(arr[:, 0])

print(arr[1, 0:2])

print(arr[0:2, 1])

print(arr[0:2, 1:3])

print(arr[-1])

print(arr[-1, :])

print(arr[:, -1])

print(arr[::-1])

print(arr[:, ::-1])


numbers = np.array([
    [10, 20, 30, 40],
    [40, 50, 60, 70],
    [70, 80, 90, 100],
    [110, 120, 130, 140]
])

#first row
print(numbers[0])
#last row
print(numbers[-1])
#first column
print(numbers[:, 0])
#last column
print(numbers[:, -1])
#middle 2*2 sub matrux
print(numbers[1:3, 1:3])

# rows reverse
print(numbers[::-1])
#columns reverse
print(numbers[:, ::-1])

print(numbers[2, 3])
print(numbers[3, 0])
print(numbers[1:3, 1:3])