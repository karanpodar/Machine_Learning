'''
Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
'''


def find_pivot(arr):

    right_ind = len(arr)
    left_ind = 0
    mid_ind = len(arr) // 2

    while mid_ind != (right_ind or left_ind):

        if sum(arr[left_ind:mid_ind+1]) == sum(arr[mid_ind:right_ind+1]):
            return mid_ind
        else:
            if sum(arr[left_ind:mid_ind+1]) > sum(arr[mid_ind:right_ind+1]):
                if ( sum(arr[left_ind:mid_ind+1]) and sum(arr[mid_ind:right_ind+1]) ) < 0:
                    mid_ind += 1
                else:
                    mid_ind -= 1
                if mid_ind == (len(arr) // 2):
                    return -1
            else:
                if ( sum(arr[left_ind:mid_ind+1]) and sum(arr[mid_ind:right_ind+1]) ) < 0:
                    mid_ind -=1
                else:
                    mid_ind += 1
                if mid_ind == (len(arr) // 2):
                    return -1

    return -1

nums = [1,7,3,6,5,6]
print(find_pivot(nums))

nums = [1,2,3]
print(find_pivot(nums))

nums = [2,1,-1]
print(find_pivot(nums))

nums = [-1,-1,-1,-1,-1,0]
print(find_pivot(nums))