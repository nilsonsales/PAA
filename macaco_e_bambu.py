"""
Problem: O macaco e o bambu oleoso
Author: nilsonsales
"""


def is_enough(k, heights):
    prev_height = 0 #heights[0]

    #print(">> new k = {}".format(k))

    for i in range(len(heights)):
        #print("{} >= {} ?".format(heights[i] - prev_height, k))
        if(k == heights[i] - prev_height):
            k -= 1
            #print("yes, k = {}".format(k))
        elif(k < heights[i] - prev_height):
            #print("Can't jump")
            k = -1

        prev_height = heights[i]

    if(k >= 0):
        return True
    else:
        return False

def get_min_energy(heights):
    min = heights[0]
    max = heights[-1]

    k = int((max+min)/2)

    # Does binary search from first value until last
    while max > min+1:

        if(is_enough(k, heights)):
            max = k
            #print("max set")
        else:
            min = k
            #print("min set")

        # set new k value and tries again
        k = int((max + min)/2)
        #print("min = {}, max = {}".format(min, max))

    print("max = {}, min = {}".format(max, min))


    # Last test to know if the min is enough
    if(is_enough(min, heights)):
        return min

    return max


T = int(input())

for i in range(T):
    # numero de degraus
    n = int(input())

    heights = []

    heights = input().split(" ")

    for j in range(n):
        heights[j] = int(heights[j])


    min = get_min_energy(heights)

    print("Case {}: {}".format(i+1, min))
