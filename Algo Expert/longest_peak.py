def longestPeak(array):
    # Write your code here.
    longest = 0
    i = 1
    while i < len(array) - 1:       
        if array[i-1] < array[i] > array[i+1]:
            l = r = i
            while l > 0 and array[l-1] < array[l]:
                l -= 1
            while r < len(array)-1 and array[r+1] < array[r]:
                r += 1
            longest = max(longest, r-l+1)
            i = r
        else:
            i += 1
    return longest 


def longestPeak(array):
    # Write your code here.
    longest = 0

    for i in range(1, len(array)-1):
        if array[i-1] < array[i] > array[i+1]:
            l = r = i

            while l > 0 and array[l-1] < array[l]:
                l -= 1

            while r < len(array)-1 and array[r+1] < array[r]:
                r += 1

            longest = max(longest, r-l+1)
    return longest 