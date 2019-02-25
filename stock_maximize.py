# Problem: Stock Maximize Problem


def get_max_pos(init, shares):
    max = 0
    max_position = 0
    for i in range(init, len(shares)):
        if shares[i] > max:
            max = shares[i]
            max_position = i
    return max_position


def get_profit(init, end, shares):
    profit = 0
    n_shares = 0

    # BUYING SHARES
    # iterates the subarray that goes from
    # init until the element before the maximim value
    for item in shares[init:end]:
        profit -= item
        n_shares += 1
    
    # SELLING SHARES
    # sell the shares at the max value
    profit += (n_shares * shares[end])

    return profit


def max_profit(n, shares):
    profit = 0
    init = 0

    while init < len(shares)-1:
        max_i = get_max_pos(init, shares)
        print("Max at #", max_i)

        profit += get_profit(init, max_i, shares)

        print("Current profit: ", profit)

        init = max_i + 1

    return profit


# Number of days
n = int(input())

# Share prices
shares = input().split(" ")

for i in range(n):
    shares[i] = int(shares[i])

print("Maximum profit: ", max_profit(n, shares))
