# /Program to multiply two square matrices of any order

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

product = np.dot(A, B)

print("Matrix Product:\n", product)

#/inverse of a matrix using numpy
# Program to find the inverse of a square matrix using numpy

import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

inv_A = np.linalg.inv(A)

print("Inverse of matrix A:\n", inv_A)


# Program to find inverse of 3x3 matrix

import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

inv_A = np.linalg.inv(A)

print("Inverse of matrix A:\n", inv_A)

# Program to find eigenvalues of a 3x3 matrix
# Program to find eigenvalues and eigenvectors of a 3x3 matrix using numpy
import numpy as np

A = np.array([[4, -2, 1],
              [0, 3, -1],
              [0, 0, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)