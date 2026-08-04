import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr)

new_arr = arr.reshape(2, 3)

print(new_arr)


arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = arr.reshape(2, -1)
print(new_arr)
arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = arr.reshape(-1, 2)
print(new_arr)

#flatten
arr = np.array([
    [1,2],
    [3,4]
])

flat = arr.flatten()

flat[0] = 100

print(arr)
print(flat)

#ravel
arr = np.array([
    [1,2],
    [3,4]
])

flat = arr.ravel()

flat[0] = 100

print(arr)
print(flat)