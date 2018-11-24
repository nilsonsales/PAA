"""
Problem: Ajude Seu Madruga
Author: nilsonsales
"""


##### GLOBAL #####
precision = 100000
delta = 1
##################


def get_dif(height, pivot):
    if (height - pivot) <= 0:
        return 0
    return height - pivot


def get_max(heights):
    return max(heights)


def sum_heights(heights, pivot):
    total = 0
    for element in heights:
        total += get_dif(element, pivot)
    return total


# Faz uma busca binaria pra achar o ponto de corte
def search_cut_point(heights, A):

    min = 0
    max = get_max(heights)

    pivot = int((min+max)/2)

    while(min <= max):

        # compara todos os elementos com o pivot
        total = sum_heights(heights, pivot)

        #print(min, max)
        #print("pivot = {}, soma = {}".format(pivot, total))

        # atualiza max e min
        if total == A:
            return pivot, total
        elif total < A:
            max = pivot-1
        else:
            min = pivot+1

        pivot = int((min+max)/2)

    #print("Solucao: point = {}, soma = {}".format(min, total/precision))
    #print(min, max)

    return min, total


def calculate_height(heights, A):
    A *= precision
    total = 0

    for element in heights:
        total += element

    # Se a soma ja for A, nao precisa cortar
    if(total == A):
        print(":D")
    # Se a soma for menor, nao tem como obter o valor
    elif(total < A):
        print("-.-")
    # Senao, calcula o valor do ponto de corte mais proximo
    else:
        cut_point, total = search_cut_point(heights, A)

        if(total == A or total+delta == A or total-delta == A ):
            print("{0:.4f}".format(cut_point/precision))

        else:
            print("-.-")


N, A = map(int, input().split(" "))

while(N != 0 and A != 0):

    heights = []

    heights = input().split(" ")

    for i in range(N):
        heights[i] = int(heights[i])*precision

    # Chama a funcao principal
    calculate_height(heights, A)

    # Espera por novos valores
    N, A = map(int, input().split(" "))
