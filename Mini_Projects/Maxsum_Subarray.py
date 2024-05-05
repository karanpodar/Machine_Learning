def maxSubArray(nums: list[int]) -> int:
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        
        maxSum = max(maxSum, curSum)
        curSum = maxSum
    return maxSum 

a = [10, 1, 4, -1, 9, 6, -7]
b = [10, 1, 4, -1, -30, 9, 6, -7, -1, 1]
c = [-4, -1, -2, -3]

print(maxSubArray(a))
print(maxSubArray(b))
print(maxSubArray(c))