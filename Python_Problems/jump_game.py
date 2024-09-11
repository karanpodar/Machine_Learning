'''
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # n = len(nums) - 1
        # jump = 0
        # if nums[0] == 0 and n == 0:
        #     return True
        # while jump < n:      
        #     if nums[jump] == 0:
        #         return False
        #     else:
        #         jump += nums[jump]
        # return True
        
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


sol = Solution()
nums = [0]
print(sol.canJump(nums))
nums = [2,3,1,1,4]
print(sol.canJump(nums))
nums = [3,2,1,0,4]
print(sol.canJump(nums))
nums = [2,0]
print(sol.canJump(nums))