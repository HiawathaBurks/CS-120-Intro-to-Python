###Need to use the power in our equation
import math

def falling_distance(falling_time):
    distance = float((0.50)*(9.80)*(pow(falling_time,2)))
    return distance

for x in range(1,10):
    print('The distance in meters for an object falling for',x,'is:',falling_distance(x))
