"""
Problem: Onde esta o marmore?
Author: nilsonsales
"""


# Number of marbles and number of queries
N, Q = map(int, input().split(" "))

marble_numbers = []
query_values = []
case = 1

while(N != 0 and Q != 0):

    # Filling the lists
    for i in range(N):
        marble_numbers.append(int(input()))

    marble_numbers.sort()

    for n in range(Q):
        query_values.append(int(input()))

    # Searching the numbers
    print("CASE# {}:".format(case))
    for query in query_values:
        found = False

        for i in range(N):
            if(query == marble_numbers[i]):
                print("{} found at {}".format(query, i+1))
                found = True
                break
        if(not found):
            print("{} not found".format(query))

    case += 1
    marble_numbers = []
    query_values = []
    N, Q = map(int, input().split(" "))
