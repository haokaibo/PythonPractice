def mergeOverlappingIntervals(intervals):
    # Write your code here.
    """
    Solution: Time: O(nlog(n)) Space: O(n)
    0: sort the array first, based on the first element of each array element
    1. The invervals array is a ordered list in ascending order.
    2. The judgement of the overlaping of adjacent intervals is 
    the last element of the previous inverval is equal or greater than the first element in the current interval
    3. Then a merge interval generated. Take care of the inital and end elements in the new merged interval.
    """

    intervals.sort(key = lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][0] = min(merged[-1][0], intervals[i][0])
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    
    return merged
