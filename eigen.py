import numpy as np

A = np.array([[4, -2, 1],
              [0, 3, -1],
              [0, 0, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
