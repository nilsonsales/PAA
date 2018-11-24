"""
Problem: BITMAP
Author: nilsonsales
"""


def analyse_bitmap(A, L_init, L, C_init, C):
    #print("Entrou A[][] = {}".format(A[L_init][C_init]))
    print("L_init {}, L {}".format(L_init, L))
    flag = True
    my_map = ""

    for i in range(L_init, L):
        for j in range(C_init, C):
            print(A[i][j])

    for i in range(L_init, L):
        for j in range(C_init, C):
            if A[i][j] != A[L_init][C_init]:
                flag = False

    if flag:
         print("All equal")
         print("print={}".format(A[L_init][C_init]))
         return str(A[L_init][C_init])

    else:
        my_map = "D"

        if(L % 2 == 0):
            L1_init = 0
            L1 = int(L / 2)
            L2_init = L1
            L2 = L
        else:
            L1_init = L_init
            L1 = int(L / 2)+1
            L2_init = L1
            L2 = L

        if (C % 2 == 0):
            C1_init = C_init
            C1 = int(C / 2)
            C2_init = C1
            C2 = C
        else:
            C1_init = C_init
            C1 = int(C / 2)+1
            C2_init = C1+1
            C2 = C


        # Q1
        print("#Q1, line from {} to {}, col {} to {}".format(L1_init, L1, C1_init, C1))
        my_map += analyse_bitmap(A, L1_init, L1, C1_init, C1)
        # Q2
        if(C-C_init >= 1):
            print("#Q2, line from {} to {}, col {} to {}".format(L1_init, L1, C2_init, C2))
            my_map += analyse_bitmap(A, L1_init, L1, C2_init, C2)
        # Q3
        if(L-L_init >= 2):
            print("#Q3, line from {} to {}".format(L2_init, L2))
            my_map += analyse_bitmap(A, L2_init, L2, C1_init, C1)
        # Q4
        if(L-L_init>=2 and C-C_init>=1):
            print("#Q4, line from {} to {}".format(L2_init, L2))
            my_map += analyse_bitmap(A, L2_init, L2, C2_init, C2)

        return my_map


# n casos de testes
n = int(input())

for i in range(n):

    L, C = map(int, input().split(" "))

    # initializing matrix
    A = [None] * L
    # Filling matrix
    for j in range(L):
        A[j] = input()

    #print(A)

    print(analyse_bitmap(A, 0, L, 0, C))

