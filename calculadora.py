""""
Problem: CALCULADORA
Author: nilsonsales
"""

result = float(input())
n2 = float(input())
op = input()

while(op != "&"):
    try:
        if op == '+':
            result = result + n2
        elif op == '-':
            result = result - n2
        elif op == '*':
            result = result * n2
        elif op == '/':
            result = result / n2

        print('{:.3f}'.format(result))
    except:
        print("operacao nao pode ser realizada")

    n2 = float(input())
    op = input()
