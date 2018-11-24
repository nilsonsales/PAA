"""
Problem: Multiplicação de Matrizes
Author: nilsonsales
"""
import numpy as np

# NxM, and MxO matrix
n, m, o = input().split(" ")

n, m, o = int(n), int(m), int(o)

# initializing matrix
A = np.zeros([n, m])
B = np.empty([m, o])
C = np.zeros([n, o])


C = C.astype(int)

# filling the matrix
for i in range(n):
    A[i] = input().split(" ")

for i in range(m):
    B[i] = input().split(" ")

# multiplying lines times column, i for lines, j for columns
for i in range(n):
    for j in range(o):
        # loads line from A and column from B
        A_line = A[i, :]
        B_column = B[:, j]
        for k in range(m):
            C[i][j] += A_line[k] * B_column[k]

for i in range(n):
    print(*C[i, :])
