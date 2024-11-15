nums = [1,4,3]

def missingNumbers(nums):
    # Write your code here.
    count = 0
    out = []
    for i in range(1, len(nums)+3):
        if i not in nums:
            out.append(i)
            count += 1
        if count == 2:
            break
            
    return out

print(missingNumbers(nums))