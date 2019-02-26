# Problem: Stock Maximize Problem


# Gets the position of the highest element in a subarray
def get_max_pos(init, shares):
    max = 0
    max_position = 0
    for i in range(init, len(shares)):
        if shares[i] > max:
            max = shares[i]
            max_position = i
    return max_position


# Calculates the profit in a subarray, knowing that the last element is the highest
def get_profit(init, end, shares):
    subprofit = 0
    n_shares = 0

    # BUY SHARES
    # iterates the subarray that goes from
    # init until the element before the maximum value
    for item in shares[init:end]:
        subprofit -= item
        n_shares += 1
    
    # SELL SHARES
    # sell all the shares at the maximum value
    subprofit += (n_shares * shares[end])

    return subprofit


# Returns the maximum profit of the whole array
def max_profit(n, shares):
    profit = 0
    init = 0

    while init < len(shares)-1:
        # Gets the position of the maximum element to limit a subarray
        max_i = get_max_pos(init, shares)
        print("Max at #", max_i)

        profit += get_profit(init, max_i, shares)

        print("Current profit: ", profit)

        init = max_i + 1

    return profit



# Number of predicted days
n = int(input())

# Share prices
shares = input().split(" ")

for i in range(n):
    shares[i] = int(shares[i])

print("Maximum profit: ", max_profit(n, shares))
