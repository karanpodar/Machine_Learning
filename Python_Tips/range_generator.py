def my_range(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1


arr = my_range(10, 15)

print(next(arr))
print(next(arr))
print(next(arr))
