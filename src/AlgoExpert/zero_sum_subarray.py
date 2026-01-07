def zeroSumSubarray(nums):
    # Write your code here.
    """
    Solution
    1. Use a set to hold the sums in the list.
    2. Added the 0 in the set in case there is 0 value elements in the array
    2. Iterate the array, add the cumulative sum in the set.
    3. If the sums appears twice in the set, then there is a true combinations, just return true.
    """
    if nums is None or len(nums) == 0:
        return False
    
    uniqueSums = set()
    uniqueSums.add(0)
    cumulativeSum = 0
    for i, n in enumerate(nums):
        cumulativeSum += n
       
        if cumulativeSum in uniqueSums:
            return True
        else:
            uniqueSums.add(cumulativeSum)
        
    
    return False