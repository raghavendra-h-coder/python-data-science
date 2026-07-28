import numpy as np


def print_array(array):
    print(array.shape)
    print(array.ndim)
    print(array.size)
    print(array.dtype)


marks = np.array([20, 24, 19, 7, 2, 1, -1, 6])

print_array(marks)

student_details = np.array([
    [10, 'Ram', 100],
    [11, 'kesav', 80],
    [12, 'krishna', 85],
    [13, 'Raghav', 80]
])

print_array(student_details)