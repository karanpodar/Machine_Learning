# Generators are used to save time and memory but it has 0 impact if we use list

def square(num):
    for i in num:
        yield(i*i)

square_input = square([1, 2, 3, 7])
# print(square_input)        # prints as a generator and not the actual values
# print(next(square_input))  # to print 1st value of the output
# print(next(square_input))
# print(next(square_input))
# print(next(square_input))  # to print N values of the output

# print(list(square_input))  # to print all the values in the list

# to print all values of a generator using a for loop
for num in square_input:
    print(num)

#### Another way of writing a generator, using a round bracket similar to list comprehension 
square_input1 = (x*x for x in [1, 2, 3, 7])

# for num in square_input1:
#     print(num)

