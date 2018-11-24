"""
Problem: Count Sort
Author: nilsonsales
"""


my_list = []
my_list = input().split(" ")

my_list_2 = []

count = 0

i = 0
while(len(my_list) > 0):
    my_list_2.append(int(my_list[0]))
    my_list.pop(0)
    #print(my_list)
    #print(my_list_2)

    index = ""
    lowest = my_list_2[i]

    for j in range(len(my_list)):  # Finding lowest number
        count += 1
        if (int(my_list[j]) < my_list_2[i] and int(my_list[j]) < lowest):
            lowest = int(my_list[j])
            index = j
            #print("Lowest number is: ", my_list[j])

    if index != '':
        #print("index = ", index)
        #print("swapping {} for {}".format(str(my_list_2[i]), my_list[index]))
        aux = str(my_list_2[i])
        my_list_2[i] = int(my_list[index])
        my_list[index] = aux

    i += 1


for element in my_list_2:
    print(element)

print("iterations: ", count)