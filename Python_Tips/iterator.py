a = [1, 2, 3, 4]

iter_a = iter(a)

# print(dir(a))
# print(dir(iter_a))

print(list(iter_a))

for i in iter_a:
    print(i)