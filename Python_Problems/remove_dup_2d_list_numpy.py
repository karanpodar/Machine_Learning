# Importing numpy module
import numpy as np

# Initializing nested list
test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]

# Printing original list
print("The original list : " + str(test_list))

# Removing duplicates
# using numpy
res = np.unique(np.array([sub for sub in test_list]), axis=0)            # when only duplicates need to be removed without sort
res = np.unique(np.array([np.sort(sub) for sub in test_list]), axis=0)    # when sort is needed

# Printing result
print("The list after duplicate removal : " + str(res.tolist()))
