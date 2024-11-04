def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key= lambda x: x[0])
    output = []
    curr = intervals[0]
    output.append(curr)
    for next in intervals:
        _, currEnd = curr
        nextStart, nextEnd = next
        if currEnd >= nextStart:
            curr[1] = max(currEnd, nextEnd)
        else:
            curr = next
            output.append(curr)

    return output