# Understanding reshape() function in numpy

import numpy as np

''' Reshape(-1, 1)
When you use reshape(-1, 1), you are asking numpy to reshape your array with 1 column 
and as many rows as necessary to accommodate the data. 
This operation will result in a 2D array with a shape (n, 1),
where n is the number of elements in your original array.
'''

# Original array
arr = np.array([1, 2, 3, 4, 5, 6])
print('Original array shape:', arr.shape)

# Reshape array
reshaped_arr = arr.reshape(-1, 1)
print('Reshaped array shape:', reshaped_arr.shape)


''' Reshape(1, -1)
On the other hand, reshape(1, -1) reshapes your array with 1 row and 
as many columns as necessary to accommodate the data. 
This operation will result in a 2D array with a shape (1, n), 
where n is the number of elements in your original array.
'''

# Original array
arr = np.array([1, 2, 3, 4, 5, 6])
print('Original array shape:', arr.shape)

# Reshape array
reshaped_arr = arr.reshape(1, -1)
print('Reshaped array shape:', reshaped_arr.shape)