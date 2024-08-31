'''
Rotated Sorted Array -
To check if the given rotated array is sorted or not 
Input - [5, 6, 7, 1, 2, 3]
Output - Sorted, since if we rotate the last 3 elements and move it to start it is sorted
'''

def check_rotated(arr):
    count = 0
    
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            continue
        else:
            count += 1

    match count:
        case 0:
            return True
        case 1:
            if arr[-1] < arr[0]:
                return True
            else:
                return False
        case _:
            return False

Input = [5, 6, 7, 1, 2, 3]
print(check_rotated(Input))

Input = [1, 2, 3, 5, 6, 7]
print(check_rotated(Input))

Input = [5, 6, 7, 1, 2, 8]
print(check_rotated(Input))

Input = [5, 6, 7, 4, 1, 2]
print(check_rotated(Input))