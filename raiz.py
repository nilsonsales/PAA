"""
Problem: Raiz
Author: nilsonsales
"""


def elevado_a(numero, e):
    a = numero
    for i in range(1, e):
        a *= numero

    return a


def busca_binaria(a, n, parte_int=False):
    # Busca binaria de 0 ate a/2

    min = 0

    if(parte_int):
        max = 999999
        parte_int = float(parte_int)
    else:
        max = int(a)+1

    # Seta o ponto de corte no meio pra iniciar a busca
    point = int((min + max) / 2)

    while (min+1 < max):
        #print(min, max)

        if(parte_int):
            result = elevado_a(parte_int + (point/1000000), n)
        else:
            result = elevado_a(point, n)

        # Se o resultado foi maior do que o numero que vc ta procurando, seta como max
        if result > a:
            max = point
        else:
            min = point

        point = int((min + max) / 2)

    if(parte_int):
        return min/1000000
    else:
        return min


def raiz(a, n):

    parte_inteira = busca_binaria(a, n)
    #print("Parte inteira: {}".format(parte_inteira))

    parte_decimal = busca_binaria(a, n, parte_inteira)

    total = str(parte_inteira) + str(parte_decimal)[1:]

    return float(total)


Q = int(input())

for i in range(Q):
    a, n = input().split(" ")

    a = float(a)
    n = int(n)

    resp = raiz(a, n)

    print("{0:.1f}".format(resp))
