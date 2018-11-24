"""
Problem: Compotencia
Author: nilsonsales
"""

def potency(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif (exp % 2) == 0:  # Se exp par
        new_exp = (exp/2)
        p = potency(base, new_exp)

        return p*p

    else:  # Se exp impar
        new_exp = ((exp-1) / 2)
        p = potency(base, new_exp)

        return p * p * base


def calculate(N):
    new_N = potency(N,N)

    return int(new_N) % 100


N1, N2 = map(int, input().split(" "))

try:
    while(True):
        new_N1 = calculate(N1)
        new_N2 = calculate(N2)

        #print(new_N1, new_N2)

        if new_N1 > new_N2:
            print(N1)
        elif new_N2 > new_N1:
            print(N2)
        else:
            print(0)

        N1, N2 = map(int, input().split(" "))

except:
     pass
