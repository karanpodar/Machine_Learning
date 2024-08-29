'''
Search an element in a sorted and rotated Array (0 Indexed) -

Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.

Note: Find the element in O(logN) time and assume that all the elements are distinct.

Example:  

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}, key = 10   
Output : Found at index 3

# if (arr[curr_ind] < arr[curr_ind-1]) and (arr[curr_ind] < arr[0]) # match pivot
# if (arr[curr_ind] < arr[curr_ind-1]) and (arr[curr_ind] > arr[0]) #not possible
# elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] < arr[0]) #move left
# elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] > arr[0]) #move right
'''

def find_pivot(arr):

    left_ind = 0
    right_ind = len(arr) - 1
    pivot = 0
    pivot_ind = 0
    # while pivot_ind != 0:
    while left_ind <= right_ind:
        curr_ind = (left_ind + right_ind) // 2
        if arr[curr_ind] > arr[left_ind]:
            if (arr[curr_ind] < arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                pivot_ind = curr_ind
                pivot = arr[curr_ind]
                break
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                right_ind = curr_ind + 1 
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] > arr[0]):
                left_ind = curr_ind - 1

        elif arr[curr_ind] < arr[left_ind]:
            if (arr[curr_ind] < arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                pivot_ind = curr_ind
                pivot = arr[curr_ind]
                break
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                right_ind = curr_ind + 1 
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] > arr[0]):
                left_ind = curr_ind - 1

        else:
            if (arr[curr_ind] < arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                pivot_ind = curr_ind
                pivot = arr[curr_ind]
                break
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] < arr[0]):
                right_ind = curr_ind + 1 
            elif (arr[curr_ind] > arr[curr_ind-1]) and (arr[curr_ind] > arr[0]):
                left_ind = curr_ind - 1
                
    # print(pivot_ind, pivot)            
    return pivot_ind

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return None

def search_key(arr, key):

    pivot_ind = find_pivot(arr)

    sub_array1 = arr[:pivot_ind]
    sub_array2 = arr[pivot_ind:]
    # print(sub_array1)
    # print(sub_array2)

    bi_array1 = binary_search(sub_array1, key)
    bi_array2 = binary_search(sub_array2, key)

    if bi_array1 == bi_array2 == None:
        return None
    elif bi_array1 == None:
        return len(sub_array1) + bi_array2
    elif bi_array2 == None:
        return bi_array1

    return None


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]

key = 3
print(search_key(arr, key))

key = 5
print(search_key(arr, key))

key = 9
print(search_key(arr, key))

key = 10
print(search_key(arr, key))

key = 1
print(search_key(arr, key))

key = 11
print(search_key(arr, key))
