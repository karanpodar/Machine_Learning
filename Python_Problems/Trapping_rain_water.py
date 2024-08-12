'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

def trap(height: list[int]) -> int:
    if not height:
      return 0

    ans = 0
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]

    while l < r:
      if maxL < maxR:
        ans += maxL - height[l]
        l += 1
        maxL = max(maxL, height[l])
      else:
        ans += maxR - height[r]
        r -= 1
        maxR = max(maxR, height[r])

    return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))