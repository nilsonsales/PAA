"""
Problem: Pacman
Author: nilsonsales
"""


def is_even(number):
    if number % 2 is 0:
        return True
    return False


N = int(input())
curr_points = 0
max_points = 0

board = [[] for x in range(N)]

for i in range(N):
    board[i] = list(input())

#print(board)

for i in range(N):
    line = board[i]

    if is_even(i):
        for item in line:
            #print(item)
            if item == 'o':
                #print("++")
                curr_points += 1
            elif item == 'A':
                if curr_points > max_points:
                    max_points = max(max_points, curr_points)
                curr_points = 0
    else:
        #print(line[::-1])

        for item in line[::-1]:
            #print(item)
            if item == 'o':
                #print("++")
                curr_points += 1
            elif item == 'A':
                if curr_points > max_points:
                    max_points = max(max_points, curr_points)
                curr_points = 0

    # if no 'A' is found
    max_points = max(max_points, curr_points)

print(max_points)
