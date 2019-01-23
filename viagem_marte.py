"""
Problem: Viagem a Marte
Author: nilsonsales
"""


def test_fuel(m, rocket_fuel, a, b):
    #total_weight = m+rocket_fuel

    #print(total_weight)

    for i in range(len(a)):
        # taking off
        fuel_spent = round((m + rocket_fuel)/a[i], 2)
        print(fuel_spent)
        rocket_fuel = round(rocket_fuel - fuel_spent, 2)

        #print("rocket fuel at take off: ", rocket_fuel)

        if(rocket_fuel < 0):
            return -1
        
        #landing
        fuel_spent = round((m + rocket_fuel)/b[i], 2)
        print(fuel_spent)
        rocket_fuel = round(rocket_fuel - fuel_spent, 2)

        #print("rocket fuel at landing: ", rocket_fuel)

        if(rocket_fuel < 0):
            return -1
    return rocket_fuel


def calculate_fuel_quantity(m, a, b):
    initial_fuel = 1000000000  # 10^9
    left_fuel = 1

    MIN = 1
    MAX = 1000000000

    fuel = int((MIN+MAX)/2)

    while(left_fuel != 0.0):
        left_fuel = test_fuel(m, fuel, a, b)

        if(left_fuel < 0):
            MIN = left_fuel
        elif(left_fuel > 0):
            MAX = left_fuel

        fuel = int((MIN + MAX)/2)
        




# number of planets to visit
n = int(input())

# rocket weight
m = int(input())

# tonnes that can be taken off with 1T of fuel
a = [int(x) for x in input().split(" ")]

# tonnes that can be landed with 1T of fuel
b = [int(x) for x in input().split(" ")]


#print(a, b)

calculate_fuel_quantity(m, a, b)
