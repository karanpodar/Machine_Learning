# Python3 code to demonstrate
# removing duplicate sublist
# using set() + sorted()

# Initializing list
test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
			[1, 2, 3], [3, 4, 1]]

# Printing original list
print("The original list : " + str(test_list))

# Removing duplicate sublist
# using set() + sorted()
res = list(set(tuple(sorted(sub)) for sub in test_list))    # when sort is needed
res = list(set(tuple(sub) for sub in test_list))      # when only duplicates need to be removed without sort

# Printing result
print("The list after duplicate removal : " + str(res))
