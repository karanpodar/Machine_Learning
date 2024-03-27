"""
Log fold distance - in this we take log of divided values and sum all the values in the array and find average of it


"""

import math
import numpy as np

a = [1, 2, 3, 8]
b = [4, 8, 0, 9]

def log_fold(a, b):
    sum = 0
    for i in a:
        for j in b:
            sum =+ abs(math.log(np.divide(i + 1 , j + 1)))     # +1 to handle 0 values
    return sum / len(a)

print(log_fold(a, b))