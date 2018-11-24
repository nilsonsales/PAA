"""
Problem: Count Sort
Author: nilsonsales
"""


my_list = []

my_list = input().split(" ")

count = 0

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

#my_list.sort()

for i in range(len(my_list)-1):
    for j in range(i+1, len(my_list)):
        count += 1
        if my_list[i] > my_list[j]:
            aux = my_list[j]
            my_list[j] = my_list[i]
            my_list[i] = aux

for element in my_list:
    print(element)

print(count)