"""
Problem: Produto simples
Author: nilsonsales
"""

PROD = 1

while True:
    try:
        PROD *= int(input())
    except EOFError:
        print('Prod = %d' % PROD)
        break
