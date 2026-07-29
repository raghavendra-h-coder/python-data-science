import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

#multiplication
print(np.dot(A, B))

#@symbol for multiplication
print(A @ B)


matrix = np.array([
    [1,2,3],
    [4,5,6]
])

#matrix transpose
print(matrix.T)

#generates identity matrix with 3 rows and 3 columns
print(np.eye(3))

A = np.array([
    [1,2],
    [3,4]
])

#determinant
print(np.linalg.det(A))

A = np.array([
    [1,2],
    [3,4]
])

#inverse
print(np.linalg.inv(A))

A = np.array([
    [1,2],
    [3,4]
])

v = np.array([5,6])

#matrix multiplication with vector
print(np.dot(A, v))


#captcha
A = np.array([
    [2,3],
    [4,5]
])

B = np.array([
    [1,2],
    [3,4]
])

print(np.dot(A, B))
print(A @ B)


matrix = np.array([
    [10,20,30],
    [40,50,60]
])

print(matrix)
print(matrix.T)
print(matrix.shape)
print(matrix.T.shape)

print(np.eye(4))

A = np.array([
    [2,1],
    [5,3]
])

print(np.linalg.det(A))
print(np.linalg.inv(A))