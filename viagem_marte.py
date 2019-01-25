"""
Problem: Viagem a Marte
Author: nilsonsales
"""

delta = round(0.01, 4)


def test_fuel(m, rocket_fuel, a, b):

    for i in range(len(a)):
        # TAKING OFF
        fuel_spent = (m + rocket_fuel) / a[i]
        rocket_fuel -= fuel_spent
        #print("rocket fuel at take off: ", rocket_fuel)

        if(rocket_fuel < 0-delta):
            return -1

        # LANDING
        fuel_spent = (m + rocket_fuel) / b[i]
        rocket_fuel -= fuel_spent
        #print("rocket fuel at landing: ", rocket_fuel)

        if(rocket_fuel < 0-delta):
            return -1
    return rocket_fuel


def calculate_fuel_quantity(m, a, b):
    left_fuel = 1

    MIN = round(0, 2)
    MAX = round(1000000000, 2)
    ZERO = round(0.00, 2)

    # first test to know if it's impossible
    fuel = MAX
    left_fuel = test_fuel(m, fuel, a, b)
    if left_fuel == -1:
        return -1

    #for i in range(100):
    while(MIN != MAX-delta):
        fuel = round((MIN + MAX)/2, 8)

        left_fuel = round(test_fuel(m, fuel, a, b), 8)
        #print(MIN, MAX, fuel, left_fuel)

        # No need to complete the loop if finds the answer
        if left_fuel == 0.0000:
            return fuel

        # updates the values
        if(left_fuel < ZERO):
            MIN = fuel
        elif(left_fuel >= ZERO):
            MAX = fuel

    # test with both values and see which is the correct
    if (test_fuel(m, MAX, a, b) == ZERO):
        #print(test_fuel(m, MAX, a, b))
        return MAX
        
    return MIN


# number of planets to visit
n = int(input())

# rocket weight
m = int(input())

# tonnes that can be taken off with 1T of fuel
a = [int(x) for x in input().split(" ")]

# tonnes that can be landed with 1T of fuel
b = [int(x) for x in input().split(" ")]

#print(a, b)

fuel = calculate_fuel_quantity(m, a, b)

if fuel > 0:
    print("{0:.2f}".format(fuel))
else:
    print("-1")
