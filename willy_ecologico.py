"""
Problem: Willy Ecologico
Author: nilsonsales
"""


# number of trees and required amount of wood
n, m = map(int, input().split(" "))

#print(n, m)


trees_height = input().split(" ")

trees_height = list(map(int, trees_height))

amount = 0

trees_height.sort()

# index where to cut
position = n-1

#print("Initial height to cut: {}".format(height_to_cut))

while(amount < m and position >= 0):
    amount = 0  # clears the amount of wood to recalculate
    diff = 0
    for element in trees_height:
        diff = element - trees_height[position]

        if(diff < 0):
            diff = 0

        amount += diff

    #print("Amount in height {} is {}".format(trees_height[position], amount))

    # shift to the next tree
    if(amount < m):
        position -= 1

# Did not get the correct amout, so chooses the lowest height (1st position)
if(position < 0):
    position = 0

print(trees_height[position])
