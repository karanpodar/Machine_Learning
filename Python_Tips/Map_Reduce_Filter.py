# MAP
def cube(x):
    return x*x*x

print(cube(2))

l1 = [1, 2, 3, 4, 5, 6]

# to create a list of cube of all values in l1 we can use for loop
# to avoid that we can use map function which will map any function to new list

l2 = list(map(cube, l1))

print(l2)

# FILTER
def greater_than(a):
    return a>4

# If we want to filter values using any function we can use filter function to call any function and filter values based on it
l3 = list(filter(greater_than, l1))

print(l3)

# REDUCE
from functools import reduce
# To reduce the input and perform any function on it we se reduce

my_input = [1, 2, 10, 5, 6, 8]

# It will reduce the my_input as 2 values and sum it until all the the values are summed
sum_out = reduce(lambda x, y: x + y, my_input)

print(sum_out)