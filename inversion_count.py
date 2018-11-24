"""
Problem: Inversion Count
Author: nilsonsales
"""


def number_of_inversions(A):
    total_inv = 0
    curr_inv = 0
    max = A[-1]
    min = A[-1]

    for i in range(len(A)-2, -1, -1):  # Começa do penultimo e vai ate o primeiro
        prev_inv = curr_inv
        curr_inv = 0

        #print("# {}".format(A[i]))
        #print("i = ", i)

        if (A[i] > max):  # se atual for o max, entao trocara com todos os prox
            #print("{} eh o max".format(A[i]))
            max = A[i]
            curr_inv = (len(A)-1) - i
        elif (A[i] < min):
            min = A[i]
            curr_inv = 0
        elif (A[i] == A[i+1]):
            curr_inv = prev_inv
        else:
            #print("Nao eh o max, tem que olhar os proximos...")
            for j in range(i+1, len(A)):
                #print("j = ", j)
                if (A[i] > A[j]):
                    #print("{} eh maior que {}".format(A[i], A[j]))
                    curr_inv += 1

        #print("{} inversoes".format(curr_inv))

        total_inv += curr_inv

    return total_inv


# Main

t = int(input())

for i in range(t):
    blank_line = input()

    A = []
    n = int(input())

    for j in range(n):
        A.append(int(input()))

    print(number_of_inversions(A))
