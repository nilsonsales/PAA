"""
Problem: Planejando a Expedição
Author: nilsonsales
"""


def get_max_number_days(N, M, food_dict):
    max_days = 0

    for i in range(int(M/N)):
        max_days += 1
        availability = 0

        for element in food_dict:
            availability += int(element/max_days)

        if availability < N:
            return max_days-1

    return max_days


# Number of participants and number of food packages
N, M = map(int, input().split(" "))

food_types = [int(x) for x in input().split(" ")]

# counting the number of elements for each type of food
my_dictionary = [0 for i in range(max(food_types)+1)]

for food in food_types:
    my_dictionary[food] += 1

# deleting empty values
food_dict = []
for i in range(len(my_dictionary)):
    if my_dictionary[i] > 0:
        food_dict.append(my_dictionary[i])

#print(food_dict)

if int(M/N) < 1:
    print(0)
else:
    print(get_max_number_days(N, M, food_dict))
