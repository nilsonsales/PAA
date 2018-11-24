"""
Problem: Multiplicação de Matrizes
Author: nilsonsales
"""

# NxM, and MxO matrix
n, m, o = input().split(" ")

n, m, o = int(n), int(m), int(o)

# initializing matrix
A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(o)] for j in range(m)]
C = [[0 for i in range(o)] for j in range(n)]

# filling the matrix
for i in range(n):
    A[i] = input().split(" ")

for i in range(m):
    B[i] = input().split(" ")

# multiplying lines times column, i for lines, j for columns
for i in range(n):
    for j in range(o):
        # loads line from A and column from B
        A_line = A[i]
        B_column = [row[j] for row in B]

        for k in range(m):
            C[i][j] += int(A_line[k]) * int(B_column[k])

for i in range(n):
    print(*C[i])
